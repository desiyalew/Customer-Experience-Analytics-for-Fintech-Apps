-- create_schema.sql

-- Drop tables if they exist (Optional)
-- DROP TABLE reviews;
-- DROP TABLE banks;

-- Table: banks
-- Stores information about each bank
CREATE TABLE banks (
    bank_id NUMBER PRIMARY KEY,
    bank_name VARCHAR2(50) UNIQUE NOT NULL
);

-- Table: reviews
-- Stores user reviews with sentiment and theme analysis
CREATE TABLE reviews (
    review_id NUMBER PRIMARY KEY,
    bank_id NUMBER NOT NULL,
    rating NUMBER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text CLOB NOT NULL,
    sentiment_label VARCHAR2(10),
    sentiment_score NUMBER(5,4),
    review_date DATE,
    theme VARCHAR2(200),
    CONSTRAINT fk_bank FOREIGN KEY (bank_id) REFERENCES banks(bank_id)
);