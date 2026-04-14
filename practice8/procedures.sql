-- 1. UPSERT (insert or update)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;


-- 2. DELETE
CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value OR phone = p_value;
END;
$$;


-- 3. BULK INSERT + validation
CREATE OR REPLACE PROCEDURE insert_many()
LANGUAGE plpgsql AS $$
DECLARE
    rec RECORD;
BEGIN
    FOR rec IN SELECT * FROM temp_contacts LOOP
        IF length(rec.phone) >= 10 THEN
            INSERT INTO contacts(name, phone)
            VALUES(rec.name, rec.phone);
        ELSE
            RAISE NOTICE 'Invalid phone: %', rec.phone;
        END IF;
    END LOOP;
END;
$$;