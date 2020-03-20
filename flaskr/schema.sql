drop table post_follow;
drop table user_follow;
drop table user_block;
drop table post;
drop table user;

create table user (
    id integer primary key autoincrement,
    username text not null,
    password text not null,
    created integer not null, --Unix time, e.g. seconds since 1970-01-01 00:00:00 UTC
    status integer not null,
    email text not null,
    default_location text not null,
    age integer not null
);

create table post (
    id integer primary key autoincrement,
    user text not null,
    parent integer not null default(0),
    created integer not null, --Unix time, e.g. seconds since 1970-01-01 00:00:00 UTC
    edited integer, --Unix time, e.g. seconds since 1970-01-01 00:00:00 UTC
    location text not null,
    content text not null,
    item text not null,
    tags text,
    ats text,
    status integer not null,

    foreign key (user) references user(id) on delete cascade on update cascade
);

create table post_follow (
    user integer not null,
    post integer not null,
    created integer not null,

    foreign key (user) references user(id) on delete cascade on update cascade
    foreign key (post) references post(id) on delete cascade on update cascade
);

create table user_follow (
    user integer not null,
    follow integer not null,
    created integer not null,

    foreign key (user) references user(id) on delete cascade on update cascade
    foreign key (follow) references user(id) on delete cascade on update cascade
);

create table user_block (
    user integer not null,
    block integer not null,
    created integer not null,

    foreign key (user) references user(id) on delete cascade on update cascade
    foreign key (block) references user(id) on delete cascade on update cascade
);