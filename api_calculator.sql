show databases;

use api_calculator;

show tables;

create table category(
	cat_id integer auto_increment ,
    cat_name varchar(200) not null,
    constraint pk_category primary key(cat_id)
);
drop table category;
desc category;


create table category_stream(
	cat_id integer not null ,
    stream varchar(500) not null ,
    constraint pk_category_stream primary key(cat_id,stream),
    constraint fk_category_stream foreign key(cat_id) references category(cat_id)
);
drop table category_stream;

desc category_stream;

create table api(
	cat_id integer not null,
    stream varchar(500) not null,
    nature_of_activity varchar(750) not null,
	max_score integer not null,
	self_assessment integer ,
	verified_api_score integer ,
    constraint fk_api foreign key (cat_id,stream) references category_stream(cat_id,stream),
	constraint pk_api primary key(cat_id,stream,nature_of_activity) 
);


drop table api;
desc api;

# Starting filling the tables and if filling goes right we will make a repo.

insert into category values(1,"Teaching Learning And Evaluation Related Activities");
insert into category values(2,"Co-Curricular,Extension and Professional Developement Related Activities");
insert into category values(3,"Research and Academic Contributions");

insert into category_stream values(1,"Mixed");
insert into category_stream values(2,"Mixed");
insert into category_stream values(3,"E/A/VS/S/MS");
insert into category_stream values(3,"FOLA/H/SS/L/PEM");

select * from category_stream;

insert into api(cat_id,stream,nature_of_activity,max_score) values(1,"Mixed","Lectures, seminars, tutorials, 
practicals, contact hours undertaken as percentage of lectures allocated",50);
insert into api(cat_id,stream,nature_of_activity,max_score) values(1,"Mixed","Lectures or other teaching duties 
in excess of the UGC norms",10);
insert into api(cat_id,stream,nature_of_activity,max_score) values(1,"Mixed","Preparation and Imparting of 
knowledge as per curriculum; syllabus enrichment by providing additional resources to students",20);
insert into api(cat_id,stream,nature_of_activity,max_score) values(1,"Mixed","Use of participatory and 
innovative teaching-learning methodologies; updating of subject content, course improvement",20);
insert into api(cat_id,stream,nature_of_activity,max_score) values(1,"Mixed","Examination duties
(Invigilation,question paper settings, evaluation of answer scripts) as per enrollment",25);

insert into api(cat_id,stream,nature_of_activity,max_score) values(2,"Mixed","Student related co-curricular,
extension and file based activities",20);
insert into api(cat_id,stream,nature_of_activity,max_score) values(2,"Mixed","Contribution to corporate life and 
management of the department and the institution through participation in 
academic and administrative comittees and responsibilities",15);
insert into api(cat_id,stream,nature_of_activity,max_score) values(2,"Mixed","Professional Developement activities
such as participation in seminars, conferences, short term, training courses, talks, lectures etc",15);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Referred Journals",15);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Non-referred but recognized 
and reputable journals and periodicals having ISBN/ISSN numbers",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Conference Proceedings as 
full papers excluding abstracts",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Text or Reference Books Published 
by International publishers with an established peer review system per sole author",50);
insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Text or Reference Books Published 
by International publishers with an established peer review system per chapter edited",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Subject Books by national
level publishers/State and Central Govt. Publications with ISBN/ISSN numbers per sole author ",25);
insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Subject Books by national
level publishers/State and Central Govt. Publications with ISBN/ISSN numbers per chapter edited ",5);


insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Subject books by other local
publishers with ISBN/ISSN numbers per sole author",15);
insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Subject books by other local
publishers with ISBN/ISSN numbers per chapter edited",3);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Chapters contributed to edited 
knowledge based volumes published by International Publishers",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Chapters in knowledge based 
volumes by Indian/National level publishers with ISBN/ISSN numbers and with numbers of national and
international directories",5);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Major Projects amount 
mobilized with grants above 30.0 lakhs",20);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Major Projects amount 
mobilized with grants above 5.0 lakhs up to 30.00 lakhs",15);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Minor Projects amount 
mobilized with grants above Rs. 50,000 up to Rs. 5 lakh",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Amount mobilized with 
minimum of Rs.10.00 lakh",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Completed project
Report(Acceptance from funding agency) per major project",20);
insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Completed project
Report(Acceptance from funding agency) per minor project",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Patent/Technology
transfer/Product/Process at national level",30);
insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Patent/Technology
transfer/Product/Process at International level",50);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","M.Phil degree awarded",3);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Ph.D degree awarded",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Ph.D Thesis Submitted",7);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Refresher courses, Methodology
workshops, Training, Teaching-Learning-Evaluation Technology Programmes, Soft Skills development Programmes,
Faculty Development Programmes for not less than two weeks",20);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Refresher courses, Methodology
workshops, Training, Teaching-Learning-Evaluation Technology Programmes, Soft Skills development Programmes,
Faculty Development Programmes for one week",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Participation and Presentation 
of research papers (oral/poster) in International Conference",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Participation and Presentation 
of research papers (oral/poster) in National Conference",7.5);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Participation and Presentation 
of research papers (oral/poster) at Regional/State level",5);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Participation and Presentation 
of research papers (oral/poster) at College Level",3);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Invited lectures or 
presentations for conferences/symposia at International Level",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"E/A/VS/S/MS","Invited lectures or 
presentations for conferences/symposia at National Level",5);



insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Referred Journals",15);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Non-referred but recognized 
and reputable journals and periodicals having ISBN/ISSN numbers",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Conference Proceedings as 
full papers excluding abstracts",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Text or Reference Books Published 
by International publishers with an established peer review system per sole author",50);
insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Text or Reference Books Published 
by International publishers with an established peer review system per chapter edited",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Subject Books by national
level publishers/State and Central Govt. Publications with ISBN/ISSN numbers per sole author ",25);
insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Subject Books by national
level publishers/State and Central Govt. Publications with ISBN/ISSN numbers per chapter edited ",5);


insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Subject books by other local
publishers with ISBN/ISSN numbers per sole author",15);
insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Subject books by other local
publishers with ISBN/ISSN numbers per chapter edited",3);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Chapters contributed to edited 
knowledge based volumes published by International Publishers",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Chapters in knowledge based 
volumes by Indian/National level publishers with ISBN/ISSN numbers and with numbers of national and
international directories",5);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Major Projects amount 
mobilized with grants above 5.0 lakhs",20);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Major Projects amount 
mobilized with grants above 3.0 lakhs up to 5.0 lakhs",15);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Minor Projects amount 
mobilized with grants above Rs. 25,000 up to Rs. 3 lakh",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Amount mobilized with 
minimum of Rs.2.0 lakh",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Completed project
Report(Acceptance from funding agency) per major project",20);
insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Completed project
Report(Acceptance from funding agency) per minor project",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Major Policy document 
of Govt. Bodies at national level",30);
insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Major Policy document 
of Govt. Bodies at International level",50);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","M.Phil degree awarded",3);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Ph.D degree awarded",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Ph.D Thesis Submitted",7);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Refresher courses, Methodology
workshops, Training, Teaching-Learning-Evaluation Technology Programmes, Soft Skills development Programmes,
Faculty Development Programmes for not less than two weeks",20);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Refresher courses, Methodology
workshops, Training, Teaching-Learning-Evaluation Technology Programmes, Soft Skills development Programmes,
Faculty Development Programmes for one week",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Participation and Presentation 
of research papers (oral/poster) in International Conference",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Participation and Presentation 
of research papers (oral/poster) in National Conference",7.5);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Participation and Presentation 
of research papers (oral/poster) at Regional/State level",5);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Participation and Presentation 
of research papers (oral/poster) at College Level",3);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Invited lectures or 
presentations for conferences/symposia at International Level",10);

insert into api(cat_id,stream,nature_of_activity,max_score) values(3,"FOLA/H/SS/L/PEM","Invited lectures or 
presentations for conferences/symposia at National Level",5);

select * from api;


# Possible Cases 
#1. Get all activities for a particular category.
#2. Get maximum score for categories.
#3. Make formulas to calculate api.
#4. Get categories with different streams
#5. Get activities which combine to form one max score.


#1.
select nature_of_activity from api where cat_id=3 ; 

#2.
select max_score from api;

#3.
# Formula  - (max_score - self_assessment) +  V_api 
 
#4.
select  * from category_stream;


#5. 
select * from api where nature_of_activity like "Participation and Presentation%";

desc api;