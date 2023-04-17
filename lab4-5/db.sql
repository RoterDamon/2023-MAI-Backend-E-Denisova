
CREATE TABLE artist (
artist_id serial PRIMARY KEY,
name_artist TEXT unique not NULL
);

INSERT INTO artist(name_artist)
values ('Nouname N. N.');

CREATE TABLE genre (
genre_id serial PRIMARY KEY,
name_genre TEXT unique not NULL
);

INSERT INTO genre(name_genre)
VALUES
('Animalistics'),
('Architecture'),
('Battle Painting'),
('Cityscape'),
('Seascape'),
('Still Life'),
('Nude'),
('Landscape'),
('Portrait'),
('Animalistic'),
('Allegorical'),
('Symbolic'),
('Everyday'),
('Historical'),
('Mythological');

CREATE TABLE city (
city_id serial PRIMARY KEY,
name_city
TEXT unique not NULL
);

INSERT INTO city(name_city)
VALUES ('Moscow'),
('Saint Petersburg'),
('Vladivostok'),
('Tolyatti'),
('Chekhov'),
('Sevastopol'),
('Kazan'),
('Yekaterinburg'),
('Krasnodar'),
('Kaliningrad'),
('Rostov-on-Don'),
('Novosibirsk'),
('Nizhny Novgorod'),
('Chelyabinsk'),
('Ufa');

create table client_role(
role_id serial PRIMARY key,
name_role TEXT unique not NULL
);

insert into client_role(name_role)
values ('admin'), ('user');

CREATE TABLE client (
client_id serial PRIMARY KEY,
name_client TEXT not NULL,
email TEXT unique not null,
client_password text not null,
city_id INT not NULL,
role_id INT not NULL,
FOREIGN KEY (city_id) REFERENCES city (city_id),
foreign key (role_id) references client_role (role_id)
);

INSERT INTO client(name_client, email, city_id, client_password, role_id)
VALUES
('Roter Damon', 'roterdamon@test', 1, 'gbdyjqrji', 1),
('Заиц Георгий', 'depish@test', 4, 'major666', 2),
('Артов Андрей', 'artoff@test', 10, 'hamelion', 2);

CREATE TABLE art (
art_id serial PRIMARY KEY,
name_pic TEXT unique not NULL,
artist_id INT NOT NULL,
genre_id INT NOT NULL,
creation_date date NOT NULL,
price DECIMAL(11, 2) CHECK (price >= 0.00),
FOREIGN KEY (artist_id) REFERENCES artist (artist_id),
FOREIGN KEY (genre_id) REFERENCES genre (genre_id)
);


CREATE TABLE buy (
buy_id serial PRIMARY KEY,
art_id INT not NULL,
client_id INT not NULL,
FOREIGN KEY (client_id) REFERENCES client (client_id)
);

insert into art (name_pic, artist_id, genre_id, creation_date, price)
values ('Super picture', 1, 1, '2022-10-10', 10000),
       ('Puper picture', 1, 4, '2000-03-12', 15000);
