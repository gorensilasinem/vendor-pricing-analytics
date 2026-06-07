with vendors as (
    select * from {{ ref('stg_vendors') }}
),

orders as (
    select * from {{ ref('stg_orders') }}
    where is_cancelled = false
),

vendor_metrics as (
    select
        v.vendor_id,
        v.vendor_name,
        v.country,
        v.city,
        v.cuisine_type,
        v.vendor_tier,
        v.rating,
        v.avg_prep_time_min,
        v.is_active,
        count(o.order_id)                          as total_orders,
        round(avg(o.gross_order_value), 2)         as avg_order_value,
        round(avg(o.discount_amount), 2)           as avg_discount,
        round(avg(o.affordability_score), 3)       as avg_affordability_score,
        round(avg(o.delivery_fee), 2)              as avg_delivery_fee,
        round(sum(o.net_order_value), 2)           as total_revenue,
        count(distinct o.customer_id)              as unique_customers,
        round(avg(o.item_count), 1)                as avg_items_per_order
    from vendors v
    left join orders o using (vendor_id)
    group by 1,2,3,4,5,6,7,8,9
)

select
    *,
    case
        when avg_affordability_score >= 0.7 then 'High Affordability'
        when avg_affordability_score >= 0.4 then 'Mid Affordability'
        else 'Low Affordability'
    end as affordability_segment,
    case
        when total_orders >= 200 then 'Top Performer'
        when total_orders >= 100 then 'Mid Performer'
        when total_orders >= 1  then 'Low Performer'
        else 'No Orders'
    end as performance_tier
from vendor_metrics
