--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

-- Started on 2022-05-19 10:23:40

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 209 (class 1259 OID 16402)
-- Name: fortistats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fortistats (
    fortid character varying NOT NULL,
    wins integer NOT NULL,
    winper numeric NOT NULL,
    kills integer NOT NULL,
    kd numeric NOT NULL
);


ALTER TABLE public.fortistats OWNER TO postgres;

--
-- TOC entry 3302 (class 0 OID 16402)
-- Dependencies: 209
-- Data for Name: fortistats; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fortistats (fortid, wins, winper, kills, kd) FROM stdin;
LazarLazar	800	9.4	14877	1.92
Gambit Toose	232	3.2	11221	1.61
\.


-- Completed on 2022-05-19 10:23:41

--
-- PostgreSQL database dump complete
--

