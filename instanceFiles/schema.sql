drop table if exists Posts;
create table Posts(
	PostID integer primary key autoincrement,
	Title text not null,
	Content text not null,
	Posted boolean not null,

);
drop table if exists Tags;
create table Tags(
	TagID integer primary key autoincrement,
	Name text not null
);
drop table if exists Comments;
create table Comments(
	CommentID integer primary key autoincrement,
	PostID integer not null,
	Poster text not null,
	Content text not null,
	FOREIGN KEY (PostID) references Posts(PostID)
);
drop table if exists ScheduledEvents;
create table ScheduledEvents(
    EventID integer primary key autoincrement,
    ScheduledDate Date not null,
    ScheduledTime Time,
    EventType Blob not null,
    ID integer,
);