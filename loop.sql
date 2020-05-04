declare
    city    bar.city_name%TYPE;
    bar   bar.bar_name%TYPE;
begin
    city := 'City';
    bar := 'Bar';
    FOR i IN 1..10 LOOP INSERT INTO bar (
        city_name,
        bar_name
    ) VALUES (
        TRIM(city)
        || i,
        TRIM(bar)
        || i
    );

    end loop;

end;
