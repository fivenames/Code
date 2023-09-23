-- Keep a log of any SQL queries you execute as you solve the mystery.

-- CREATE TABLE crime_scene_reports (
--     id INTEGER,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     street TEXT,
--     description TEXT,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE interviews (
--     id INTEGER,
--     name TEXT,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     transcript TEXT,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE atm_transactions (
--     id INTEGER,
--     account_number INTEGER,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     atm_location TEXT,
--     transaction_type TEXT,
--     amount INTEGER,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE bank_accounts (
--     account_number INTEGER,
--     person_id INTEGER,
--     creation_year INTEGER,
--     FOREIGN KEY(person_id) REFERENCES people(id)
-- );
-- CREATE TABLE airports (
--     id INTEGER,
--     abbreviation TEXT,
--     full_name TEXT,
--     city TEXT,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE flights (
--     id INTEGER,
--     origin_airport_id INTEGER,
--     destination_airport_id INTEGER,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     hour INTEGER,
--     minute INTEGER,
--     PRIMARY KEY(id),
--     FOREIGN KEY(origin_airport_id) REFERENCES airports(id),
--     FOREIGN KEY(destination_airport_id) REFERENCES airports(id)
-- );
-- CREATE TABLE passengers (
--     flight_id INTEGER,
--     passport_number INTEGER,
--     seat TEXT,
--     FOREIGN KEY(flight_id) REFERENCES flights(id)
-- );
-- CREATE TABLE phone_calls (
--     id INTEGER,
--     caller TEXT,
--     receiver TEXT,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     duration INTEGER,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE people (
--     id INTEGER,
--     name TEXT,
--     phone_number TEXT,
--     passport_number INTEGER,
--     license_plate TEXT,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE bakery_security_logs (
--     id INTEGER,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     hour INTEGER,
--     minute INTEGER,
--     activity TEXT,
--     license_plate TEXT,
--     PRIMARY KEY(id)
-- );

select description from crime_scene_reports where street = 'Humphrey Street' and year = 2021 and month = 7 and day = 28;
-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.

.mode csv

select name, transcript from interviews where year = 2021 and month = 7 and day = 28;
-- Ruth,"Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
-- If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame."

-- Eugene,"I don't know the thief's name, but it was someone I recognized.
-- Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money."

-- Raymond,"As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
-- In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
-- The thief then asked the person on the other end of the phone to purchase the flight ticket."

select license_plate from bakery_security_logs where year = 2021 and month = 7 and day = 28 and hour = 10 and 15 < minute < 25 and activity = 'exit';
-- 5P2BI95
-- 94KL13X
-- 6P58WS2
-- 4328GD8
-- G412CB7
-- L93JTIZ
-- 322W7JE
-- 0NTHK55
-- 1106N58


select account_number from atm_transactions where year = 2021 and month = 7 and day = 28 and atm_location = 'Leggett Street' and transaction_type = 'withdraw';
-- 28500762
-- 28296815
-- 76054385
-- 49610011
-- 16153065
-- 25506511
-- 81061156
-- 26013199

select name from people
where license_plate in (select license_plate from bakery_security_logs where year = 2021 and month = 7 and day = 28 and hour = 10 and 15 < minute < 25 and activity = 'exit');
-- Vanessa
-- Barry
-- Iman
-- Sofia
-- Taylor
-- Luca
-- Diana
-- Kelsey
-- Bruce

select name from people where id in (select person_id from bank_accounts
where account_number in (select account_number from atm_transactions where year = 2021 and month = 7 and day = 28 and atm_location = 'Leggett Street' and transaction_type = 'withdraw'));
-- Kenny
-- Iman
-- Benista
-- Taylor
-- Brooke
-- Luca
-- Diana
-- Bruce

-- repeated names Iman, Taylor, Luca, Diana and Bruce;

select caller, receiver from phone_calls where caller in
(select phone_number from people where name = 'Iman' or name = 'Taylor' or name = 'Luca' or name = 'Diana' or name = 'Bruce')
and year = 2021 and month = 7 and day = 28 and duration < 60;
-- "(367) 555-5533","(375) 555-8161"
-- "(286) 555-6063","(676) 555-6554"
-- "(770) 555-1861","(725) 555-3243"

select id from airports where city = 'Fiftyville';
-- 8

select id, from flights where origin_airport_id = 8 and year = 2021 and month = 7 and day = 29 order by hour, minute asc limit 1;
-- 36

select name, phone_number from people where passport_number in (select passport_number from passengers where flight_id = 36)
and (phone_number = "(367) 555-5533" or phone_number = "(286) 555-6063" or phone_number = "(770) 555-1861");
-- Taylor, "(286) 555-6063"
-- Bruce, "(367) 555-5533"

select name, phone_number, passport_number from people where (phone_number = "(375) 555-8161" or phone_number = "(676) 555-6554");
-- James,"(676) 555-6554",2438825627
-- Robin,"(375) 555-8161",???

-- Database missing info... However, can verify that James not in the flight, hence should be Bruce and Robin...