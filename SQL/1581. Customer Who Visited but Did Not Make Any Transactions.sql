# Write your MySQL query statement below
select customer_id, count(customer_id) as count_no_trans from Visits
where not exists
(select visit_id from Transactions
 where Visits.visit_id = Transactions.visit_id)
group by Visits.customer_id;