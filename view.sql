create view party as 
select humancocktail.human_name,
humancocktail.cocktail_name from humancocktail
join humanbar on humanbar.human_name=humancocktail.human_name
join bar on bar.bar_name=humanbar.bar_name;
