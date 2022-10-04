CREATE TABLE bears (
  id SERIAL PRIMARY KEY,
  bear_uuid uuid DEFAULT uuid_generate_v4 (),
  bear_number INTEGER UNIQUE,
  bear_name TEXT UNIQUE,
  bear_gender TEXT,
  first_identified INTEGER,
  bear_size TEXT,
  fur_description TEXT,
  muzzle_description TEXT,
  ear_description TEXT
);

CREATE TABLE rounds (
  id SERIAL PRIMARY KEY,
  round_uuid uuid DEFAULT uuid_generate_v4 (),
  competition_year INTEGER NOT NULL,
  round_number INTEGER,
  final_round BOOLEAN NOT NULL,
  UNIQUE(competition_year, round_number)
);

CREATE TABLE brackets (
  id SERIAL PRIMARY KEY,
  bracket_uuid uuid DEFAULT uuid_generate_v4 (),
  round_id INTEGER REFERENCES rounds(id),
  bracket_date DATE NOT NULL,
  first_bear INTEGER REFERENCES bears(id),
  second_bear INTEGER REFERENCES bears(id)
);

CREATE TABLE results (
  id SERIAL PRIMARY KEY,
  bracket_id INTEGER NOT NULL REFERENCES brackets(id),
  winner INTEGER NOT NULL REFERENCES bears(id),
  winner_votes INTEGER,
  runner_up_votes INTEGER
);

CREATE TABLE bracket_contestants(
	id SERIAL PRIMARY KEY,
  	bracket_contestant_uuid uuid DEFAULT uuid_generate_v4 (),
 	bracket_id INTEGER NOT NULL REFERENCES brackets(id),
  	bear_id INTEGER NOT NULL REFERENCES bears(id),
  	UNIQUE(bracket_id, bear_id)
);
