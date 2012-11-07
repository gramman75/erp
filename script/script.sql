select b.user_name
     , a.year
     , sum(case a.month
           when 1 then a.counts
           else 0
        )
from erp.xxsm_user_logins a
   , erp.xxsm_users_v b
where a.user_id = b.id
and   a.year = '2012'
group by b.user_name
     , a.year
     , a.month
limit 0, 100000     
