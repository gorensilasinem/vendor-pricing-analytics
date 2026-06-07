with source as (
    select * from raw_orders
),

cleaned as (
    select
        order_id,
        vendor_id,
        cast(order_date as date) as order_date,
        item_count,
        gross_order_value,
        delivery_fee,
        discount_amount,
        net_order_value,
        affordability_score,
        is_cancelled::boolean as is_cancelled,
        payment_method,
        customer_id
    from source
    where order_id is not null
      and gross_order_value > 0
)

select * from cleaned
