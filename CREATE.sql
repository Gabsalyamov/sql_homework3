CREATE TABLE if not exists musicians (
    id SERIAL PRIMARY KEY,
    name_musicians text,
    nickname text
);

CREATE TABLE if not exists Albums (
    id SERIAL PRIMARY KEY,
    name_album text,
    year_release_album INTEGER
);

CREATE TABLE if not exists Track (
    id SERIAL PRIMARY KEY,
    name_track text,
    duration numeric,
    album_id integer references albums(id)
);

CREATE TABLE if not exists Genre (
    id SERIAL PRIMARY KEY,
    name_genre text
);

CREATE TABLE if not exists Digets (
    id SERIAL PRIMARY KEY,
    name_digest text,
    year_release_digest INTEGER
);

CREATE TABLE if not exists Genre_musicains (
    id SERIAL PRIMARY KEY,
    genre_id integer references genre(id),
    musician_id integer references musicians(id)
);

CREATE TABLE if not exists Musicians_albums (
    id SERIAL PRIMARY KEY,
    musician_id integer references musicians(id),
    album_id integer references albums(id)
);

CREATE TABLE if not exists Composition_digets (
    id SERIAL PRIMARY KEY,
    digest_id integer references digets(id),
    track_id integer references track(id)
);
