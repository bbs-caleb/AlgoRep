with new_contacts_table as (
    select  co.*, 
            case 
                when c.customer_id is not null then 'customer'
                else null 
            end as is_customer
    from Contacts co
    left join Customers c 
        on co.contact_name = c.customer_name and co.contact_email = c.email
)

select 
        i.invoice_id,
        c.customer_name,
        i.price,
        count(co.user_id) as contacts_cnt,
        count(co.is_customer) as trusted_contacts_cnt 
from Invoices i
inner join Customers c 
    on i.user_id = c.customer_id 
left join new_contacts_table co 
    on co.user_id = c.customer_id 
group by 1, 2, 3
order by invoice_id