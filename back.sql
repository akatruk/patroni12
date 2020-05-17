--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

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
-- Name: vendor_fields; Type: TABLE; Schema: public; Owner: lsp_banking
--

CREATE TABLE public.vendor_fields (
    id bigint NOT NULL,
    name character varying NOT NULL,
    title character varying,
    type character varying,
    long_title text,
    mask character varying,
    placeholder character varying,
    required boolean,
    vendor_uuid uuid NOT NULL
);


ALTER TABLE public.vendor_fields OWNER TO lsp_banking;

--
-- Name: vendor_fields_id_seq; Type: SEQUENCE; Schema: public; Owner: lsp_banking
--

CREATE SEQUENCE public.vendor_fields_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vendor_fields_id_seq OWNER TO lsp_banking;

--
-- Name: vendor_fields_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: lsp_banking
--

ALTER SEQUENCE public.vendor_fields_id_seq OWNED BY public.vendor_fields.id;


--
-- Name: vendors; Type: TABLE; Schema: public; Owner: lsp_banking
--

CREATE TABLE public.vendors (
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone,
    uuid uuid DEFAULT public.gen_random_uuid() NOT NULL,
    acct bigint NOT NULL,
    name character varying NOT NULL,
    title character varying,
    icon character varying,
    category character varying
);


ALTER TABLE public.vendors OWNER TO lsp_banking;

--
-- Name: COLUMN vendors.acct; Type: COMMENT; Schema: public; Owner: lsp_banking
--

COMMENT ON COLUMN public.vendors.acct IS 'Идентификатор вендора';


--
-- Name: vendor_fields id; Type: DEFAULT; Schema: public; Owner: lsp_banking
--

ALTER TABLE ONLY public.vendor_fields ALTER COLUMN id SET DEFAULT nextval('public.vendor_fields_id_seq'::regclass);


--
-- Name: vendor_fields vendor_fields_pkey; Type: CONSTRAINT; Schema: public; Owner: lsp_banking
--

ALTER TABLE ONLY public.vendor_fields
    ADD CONSTRAINT vendor_fields_pkey PRIMARY KEY (id);


--
-- Name: vendors vendors_pkey; Type: CONSTRAINT; Schema: public; Owner: lsp_banking
--

ALTER TABLE ONLY public.vendors
    ADD CONSTRAINT vendors_pkey PRIMARY KEY (uuid);


--
-- Name: ix_vendors_acct; Type: INDEX; Schema: public; Owner: lsp_banking
--

CREATE INDEX ix_vendors_acct ON public.vendors USING btree (acct);


--
-- Name: vendor_fields vendor_fields_vendor_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lsp_banking
--

ALTER TABLE ONLY public.vendor_fields
    ADD CONSTRAINT vendor_fields_vendor_uuid_fkey FOREIGN KEY (vendor_uuid) REFERENCES public.vendors(uuid);


--
-- PostgreSQL database dump complete
--

