create view party as 
select humancocktail.human_name,
humancocktail.cocktail_name,
humanbar.bar_name,
bar.city_name
from humancocktail
inner join humanbar on humanbar.human_name=humancocktail.human_name
inner join bar on bar.bar_name=humanbar.bar_name;
