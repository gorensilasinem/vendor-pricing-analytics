with source as (
    select * from raw_vendors
),

cleaned as (
    select
        vendor_id,
        vendor_name,
        country,
        city,
        cuisine_type,
        vendor_tier,
        cast(joined_date as date) as joined_date,
        avg_prep_time_min,
        rating,
        is_active::boolean as is_active
    from source
    where vendor_id is not null
)

select * from cleaned
