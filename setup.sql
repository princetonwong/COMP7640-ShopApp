USE SHOPAPP;

DROP TABLE IF EXISTS Shop;

create table IF NOT EXISTS Shop (
	shopId VARCHAR(40),
	name VARCHAR(255),
	rating DECIMAL(2,1),
	location VARCHAR(255),
	PRIMARY KEY (shopId)
);

insert into Shop (shopId, name, rating, location)
values
('93d773fe-4c26-46f4-a7dc-c767fbbd266e', 'Emmerich, Ullrich and Nicolas', 3.4, '361 4th Pass'),
('07972cc1-56bd-4207-bf10-e540e5311f18', 'Lind Inc', 4.0, '49 Knutson Avenue'),
('cbf0e5fe-dd63-4bb1-8378-4eb53b218212', 'Swaniawski-Flatley', 3.9, '695 Redwing Alley'),
('2ef1ce37-30f3-4a33-8961-5798cb8e3351', 'Labadie-Oberbrunner', 3.2, '8506 North Pass'),
('9f487d76-7174-4c26-89da-b41fbe0e5898', 'Hirthe LLC', 4.6, '94857 Hoffman Alley'),
('29148be9-9bac-4ff8-b734-c5a408a96093', 'Waelchi LLC', 3.9, '08364 Vera Pass'),
('e16dee69-e170-4a17-869f-45bedba0b40a', 'Boyer, Armstrong and Bayer', 1.3, '17617 Del Mar Terrace'),
('b61bd214-da1b-499f-9469-d610d565a808', 'Kuvalis, Nicolas and Prosacco', 4.4, '79964 Thierer Way'),
('3d63b043-2214-49a4-b0a4-2927d83cf133', 'Roberts-Marquardt', 3.8, '87287 Starling Hill'),
('93ee0bd4-6381-455f-b9a5-5489d11744c4', 'Ritchie-Connelly', 1.3, '37 Thompson Point'),
('0ee5a8d7-60d1-4808-b807-9f101a1e25ad', 'Langosh-Anderson', 1.2, '617 Randy Lane'),
('9fb2048f-688f-4a3d-aa40-9f1238c25c17', 'Hackett LLC', 3.8, '0 Roth Road'),
('e1dcc339-922c-461f-a099-9635b114ccda', 'Grant Inc', 2.2, '54 Mccormick Hill'),
('da258297-9c0a-49d8-99b0-7a285519351e', 'Kreiger-Becker', 1.2, '996 Pennsylvania Crossing'),
('cc2f516a-71f7-412e-b017-72d1140ad6cd', 'Lebsack-Emard', 4.4, '5 Katie Lane'),
('a4997afa-da5a-4f7b-b5ff-d53e93a229b5', 'Jerde-Heathcote', 5.0, '46897 Hauk Plaza'),
('62fd92f6-7e9a-41cb-a850-894de40c5fec', 'Raynor-Windler', 4.9, '22 Kedzie Avenue'),
('f764038e-1a5f-45aa-87ae-63acfda92381', 'Schuster LLC', 1.4, '28629 Haas Plaza'),
('9a983393-65dd-4f6f-b625-5ff8c2558a12', 'Donnelly, Hilpert and Kassulke', 4.1, '88779 Artisan Point'),
('ff507a85-5194-41fa-bf86-f23b7b910f9b', 'Hand and Sons', 1.1, '906 Luster Road'),
('55e0a867-0125-4725-ae92-3a0a62b90e06', 'Kirlin, Schaefer and Goyette', 3.0, '80863 Fieldstone Trail'),
('9d3e2262-37c5-4d9e-b132-b078705c572b', 'Donnelly-Nader', 1.7, '567 Welch Crossing'),
('1c9ef3df-bed1-4b11-90f8-49471d0d8048', 'Johnston Group', 4.0, '3489 Hooker Crossing'),
('64e85042-8a83-4471-ba1e-1ac4fa1b7f7f', 'Reinger LLC', 1.4, '97767 Bluestem Plaza'),
('d41adf51-3c28-4b7b-992d-c54ad337fef9', 'Streich, Volkman and Senger', 3.1, '2 Clemons Hill'),
('38f4bccc-4c46-472d-a279-31ff1d5a9a83', 'Hayes-Mueller', 3.2, '51 Homewood Point'),
('7ba43b53-5532-4f67-9c95-a90e1e8fb37b', 'Tremblay-Beahan', 3.8, '48 Trailsway Way'),
('99121aa0-3c41-4097-a615-d773e2edad1b', 'Rodriguez-Toy', 4.6, '305 Continental Lane'),
('0b0aa4e3-f6e9-40f2-a9a1-e970b9827846', 'Streich, Simonis and Stiedemann', 2.7, '520 School Point'),
('0ba79a57-ba94-46e5-b732-2fb1ae43aa9f', 'Kshlerin, Donnelly and Hermann', 4.5, '111 Scofield Crossing'),
('e1d55398-20c8-4e78-b2a9-1c027f6624f7', 'Cartwright-Kilback', 2.6, '71506 Fordem Place'),
('acba3e6d-7582-4430-9091-be0eb86ed797', 'Hammes-Crist', 1.3, '4218 Stuart Circle'),
('785ce364-c0e1-4e3a-adce-aa77deb0bc4b', 'Kozey-Connelly', 1.1, '2 Rusk Lane'),
('22a306a5-de89-4444-87f6-3783e5c75da9', 'Considine-Graham', 1.5, '06538 Jay Avenue'),
('a0a834c4-406f-4d2a-a55c-c6ea7945678d', 'Reinger, Mohr and Bradtke', 2.4, '3499 Marquette Center'),
('4da93b38-96bc-4fdf-9412-aa394f4595d0', 'Wolf, Cassin and Dicki', 4.9, '693 Sauthoff Avenue'),
('9295e51c-3894-45b8-b02e-28f04b0f45f4', 'Metz, Orn and Adams', 4.1, '2830 Melody Junction'),
('5f52bdab-9fc5-4d44-8407-c7486a66bec8', 'Robel, Morissette and Shields', 4.8, '1800 Brentwood Center'),
('9af683c6-bedc-4f29-b709-20877665ccba', 'Stroman LLC', 3.7, '5267 Badeau Point'),
('f6c45600-2487-44b1-9f0d-c50d7e3e33cc', 'McClure-Reinger', 3.4, '0303 Hansons Park'),
('90d28e44-8bc2-48dd-9208-8b87f1820a56', 'Torphy-Kunde', 1.1, '701 Elmside Parkway'),
('c4247eee-4be5-4c16-a3d4-9c2386d0c56d', 'Waters-Kihn', 3.1, '883 Vermont Alley'),
('e8aa5914-1c9f-440b-9c42-7f388e1b2b2e', 'Christiansen, Jacobs and Raynor', 3.8, '59373 Brickson Park Park'),
('18d83cc9-f6a9-48de-8775-ac2b66ac50d2', 'Towne-Kemmer', 1.9, '76250 Laurel Trail'),
('1a1bcc8c-81cd-4367-a9c6-39a28dc432ed', 'Runolfsdottir-Runolfsson', 3.3, '77 Anzinger Plaza'),
('d945d035-faf0-48fc-a0a9-f2a7c91e4e11', 'Rolfson, Hamill and Rolfson', 1.9, '25 Farragut Drive'),
('7ea736cc-0462-49d4-a066-2a858975b873', 'Larkin, Dare and Spinka', 2.0, '4745 Westend Pass'),
('a8a6600e-3ed8-4b4a-a30a-12afed3f3e16', 'Boyer-Purdy', 4.5, '03131 Lien Lane'),
('035d2317-fdfb-4995-8a3c-841cffa0d755', 'Lesch-Hodkiewicz', 2.8, '5103 Birchwood Junction'),
('830106f2-da49-4cf7-8d6a-90858f30a3e5', 'Satterfield, Waters and Swaniawski', 1.3, '83 Dahle Alley')

drop table if exists Item;

create table if not exists Item(
	itemId VARCHAR(50),
	name VARCHAR(255),
	price DECIMAL(6,1),
	keyword1 VARCHAR(50),
	keyword2 VARCHAR(50),
	keyword3 VARCHAR(50),
	primary key (itemId)
);

insert into Item (itemId, name, price, keyword1, keyword2, keyword3)
values ('431c7779-4cd6-44f6-ae1c-da80a13fe633', 'GLYCERIN', 131.7, 'Yellow', 'Quamba', 'Grocery'),
('a5ac0e45-faf5-4e3d-9ad2-111c8dffe9ef', 'Titanium Dioxide, OCTINOXATE, Zinc Oxide, OCTISALATE', 157.8, 'Purple', 'Babblestorm', 'Toys'),
('88600d90-61b7-4552-a12e-c654cc5f2a52', 'TRAMADOL HYDROCHLORIDE', 194.0, 'Puce', 'Yotz', 'Sports'),
('7d49c255-b254-4734-9298-4c38c6c475c2', 'MAGNESIUM ASCORBYL PHOSPHATE', 1.0, 'Mauv', 'LiveZ', 'Baby'),
('9a94f2ed-d798-44fc-ac0a-f9b69b3d582d', 'Dimethicone', 140.7, 'Orange', 'Wikizz', 'Home'),
('5c1d9b0f-b237-47ea-b0a7-a528790283a6', 'PETROLATUM', 156.0, 'Pink', 'Roomm', 'Baby'),
('9f77f7e7-7717-4e01-aaf0-f2e5b8573f9d', 'mesalamine', 90.1, 'Puce', 'Yakidoo', 'Beauty'),
('1c7bf413-47eb-466e-bd8d-fd515615c9f1', 'mucor racemosus', 52.4, 'Puce', 'Fivebridge', 'Beauty'),
('44083444-36b3-417e-99b2-4eecf5c05506', 'Salicylic Acid', 158.2, 'Maroon', 'Demizz', 'Kids'),
('d5db2ec9-a087-4627-a872-4db5bcc9800c', 'levonorgestrel and ethinyl estradiol', 188.3, 'Yellow', 'Gabspot', 'Kids'),
('c649126d-e857-4e73-b18a-4ef1b766d487', 'salicylic acid', 157.4, 'Blue', 'Vitz', 'Grocery'),
('a8849d06-b186-4f94-ba69-d7145b9e2daa', 'ETHYL ALCOHOL', 82.7, 'Aquamarine', 'Devpulse', 'Industrial'),
('94d3400e-c2db-463c-bdb1-171b20df0a98', 'divalproex sodium', 68.5, 'Indigo', 'Aimbu', 'Baby'),
('a1ea23ce-ed9b-4975-9305-d09226e0273b', 'Simvastatin', 93.0, 'Aquamarine', 'Photobug', 'Clothing'),
('cb5b7428-a7c0-48d1-927c-c8e73a043bbc', 'Chlorpheniramine maleate and Phenylephrine HCl', 85.0, 'Puce', 'Fivespan', 'Kids'),
('148a7426-e185-4bcd-b92a-cc3a0032fae2', 'atropine sulfate', 100.3, 'Turquoise', 'Fatz', 'Garden'),
('afbc9559-e22b-4dc1-94a7-a3ed6fded7c9', 'BISMUTH SUBSALICYLATE', 123.8, 'Puce', 'InnoZ', 'Jewelry'),
('db4ba8af-4289-4e65-aac0-2dc181d38d0c', 'risperidone', 131.8, 'Purple', 'Thoughtstorm', 'Home'),
('139dc211-c0ea-43d6-aa21-4aec7f9e0291', 'Treatment Set TS332090', 157.2, 'Red', 'Twitterwire', 'Jewelry'),
('158e0b67-9130-482e-83eb-16084ca29fba', 'rOPINIRole', 96.8, 'Green', 'Quinu', 'Health'),
('8a6955d4-f153-40a0-b7c6-1fcac1f342ca', 'Guaifenesin', 74.1, 'Green', 'Eadel', 'Computers'),
('c0df5d19-27f3-4421-a87e-9d181a32d354', 'WITCH HAZEL', 189.1, 'Teal', 'Aivee', 'Home'),
('9d330a05-7a0e-42a0-b40a-f4836ee17cec', 'SULFUR, RESORCINOL', 1.9, 'Blue', 'Devpoint', 'Grocery'),
('4cc032fd-1879-4db6-8197-52b58ce7084a', 'Anticoagulant Citrate Phosphate Dextrose (CPD)', 151.5, 'Orange', 'Yodel', 'Beauty'),
('dcfc8e22-aed8-40d8-bb54-bfca1bfc0466', 'Buprenorphine and Naloxone', 184.8, 'Pink', 'Camimbo', 'Industrial'),
('3a7baa49-e0e7-4c81-b136-77776835cc2e', 'Trihexyphenidyl Hydrochloride', 147.3, 'Orange', 'Buzzster', 'Garden'),
('a7ce020e-d3de-4237-8ffa-31b57b5c7796', 'Cultivated Rye', 77.7, 'Yellow', 'InnoZ', 'Home'),
('75335cde-88cc-45df-812f-8a5448b968ed', 'Celecoxib', 150.9, 'Violet', 'Innotype', 'Industrial'),
('d11a919d-bc55-4c12-bf1f-919814ca2a4d', 'Minoxidil', 133.8, 'Blue', 'Bubbletube', 'Electronics'),
('a566e57b-f3cf-412e-ad16-f4bef9b798fc', 'Cimetidine', 130.2, 'Aquamarine', 'Meeveo', 'Automotive'),
('1a1da05a-46cb-4baa-9648-d1421e93f08a', 'AMLODIPINE BESYLATE', 183.6, 'Goldenrod', 'Skiba', 'Baby'),
('a141a179-3c5a-4c51-8161-d1f39350c3a0', 'Benzocaine, Benzethonium Chloride', 48.1, 'Teal', 'Brightbean', 'Toys'),
('79bb8750-bd0b-4ec5-835c-07b6ad3aaf10', 'CEFPROZIL', 140.6, 'Indigo', 'Trilia', 'Games'),
('09ca6a8e-842d-4b4a-b710-279396e56a70', 'Isopropyl Alcohol', 4.4, 'Mauv', 'Lazzy', 'Toys'),
('82df7427-f3ad-4702-826b-255b07d6ff9f', 'topiramate', 120.6, 'Turquoise', 'Skalith', 'Movies'),
('556a2b2c-050a-4c78-b8fb-0b3c1ccea2af', 'West Wheat Grass', 128.8, 'Red', 'Rhycero', 'Home'),
('80db28a2-fbe2-4217-a906-6d6223c01617', 'ALUMINUM CHLOROHYDRATE', 172.7, 'Turquoise', 'Eadel', 'Shoes'),
('11e91bb9-8c09-4fbf-b4ac-9041787f0d2c', 'ZONISAMIDE', 75.1, 'Aquamarine', 'Tagopia', 'Computers'),
('6bcbcc77-b321-4e9c-9dc2-eaab80b2cc96', 'dextroamphetamine sulfate', 148.8, 'Blue', 'Innojam', 'Tools'),
('e6d396bd-fc52-489c-85ba-6ff575e29b05', 'Diphenhydramine HCl', 28.4, 'Aquamarine', 'Eimbee', 'Baby'),
('f15953c4-e31e-4e34-84b3-f3016b0ce84f', 'CAMPHOR, MENTHOL AND METHYL SALICYLATE', 113.8, 'Purple', 'Livetube', 'Garden'),
('73a551cd-dbd3-4134-a1f3-fc8dcf98fd01', 'Loratadine', 110.8, 'Maroon', 'Jayo', 'Baby'),
('f347af8c-70fd-4cc7-9f15-12aaa7b20914', 'BUPIVACAINE HYDROCHLORIDE', 186.1, 'Maroon', 'Divape', 'Computers'),
('0a238f8a-c3d9-40c2-9087-6cb6703e3b40', 'Dihydroergotamine Mesylate', 139.9, 'Aquamarine', 'Shuffledrive', 'Health'),
('e92ad83c-534a-41c0-9570-34733e5c626e', 'VANCOMYCIN HYDROCHLORIDE', 94.1, 'Turquoise', 'Vinte', 'Baby'),
('c62a2994-e9b3-45b6-820d-053d4bcbab86', 'Loperamide hydrochloride', 21.4, 'Pink', 'Vitz', 'Music'),
('7ccd887f-a136-48b9-90c2-c833062e149f', 'Propranolol Hydrochloride', 171.3, 'Green', 'Twinte', 'Clothing'),
('7f9aeef7-b4ce-4347-85e2-6e3450d3e98f', 'Allergenic Extracts Alum Precipitated', 161.2, 'Goldenrod', 'Twinder', 'Garden'),
('7d2f2f91-6694-4608-bb9d-e04f71f0295b', 'Calcium Carbonate', 128.5, 'Teal', 'Vipe', 'Shoes'),
('13b18c55-1842-4780-966a-6261f481396f', 'Titanium dioxide', 172.6, 'Mauv', 'Ntags', 'Electronics')


create table if not exists Customer(
	customerId VARCHAR(50),
	name VARCHAR(50),
	phone VARCHAR(50),
	address VARCHAR(50),
	primary key (customerId)
);

insert into Customer (customerId, name, phone, address)
values
('gnotton0@gmpg.org', 'Gabriell Notton', '(659) 3699113', '14822 Sullivan Lane'),
('caskey1@about.me', 'Cam Askey', '(390) 1677544', '994 Oriole Circle'),
('ltirkin2@yellowpages.com', 'Loralee Tirkin', '(434) 6912119', '3 Crowley Terrace'),
('hyanshonok3@ucla.edu', 'Holmes Yanshonok', '(159) 1976721', '501 Killdeer Parkway'),
('hfairley4@goodreads.com', 'Hester Fairley', '(671) 3647299', '246 Elka Trail'),
('omeininking5@bravesites.com', 'Othelia Meininking', '(276) 5117234', '125 Barnett Lane'),
('cstollenberg6@sciencedaily.com', 'Chelsie Stollenberg', '(704) 8553503', '79 Karstens Drive'),
('ehasely7@ocn.ne.jp', 'Emmett Hasely', '(339) 4993593', '68 Schurz Crossing'),
('omathonnet8@nydailynews.com', 'Obie Mathonnet', '(330) 9546979', '884 Kings Drive'),
('sbrokenshaw9@creativecommons.org', 'Sybila Brokenshaw', '(246) 5178341', '7302 Merry Crossing'),
('rkennermanna@com.com', 'Renie Kennermann', '(274) 1803261', '01929 Arapahoe Lane'),
('vchaliceb@last.fm', 'Viviyan Chalice', '(882) 1289168', '9 Artisan Drive'),
('nhargc@surveymonkey.com', 'Nalani Harg', '(993) 6189860', '99 Havey Circle'),
('ehuddlesd@blogtalkradio.com', 'Eimile Huddles', '(524) 3040902', '48662 Scofield Parkway'),
('bbriscoe@mapquest.com', 'Brandtr Brisco', '(162) 2640943', '7444 Elgar Terrace'),
('jpetrollif@sina.com.cn', 'Jens Petrolli', '(511) 4143511', '83185 Marcy Court'),
('lhalfhydeg@bbb.org', 'Leopold Halfhyde', '(406) 4582851', '1791 Graceland Avenue'),
('hquanh@flavors.me', 'Hobey Quan', '(545) 8268493', '5 Mccormick Parkway'),
('kandreiai@engadget.com', 'Kial Andreia', '(825) 9511840', '58 Meadow Vale Hill'),
('gmewj@chronoengine.com', 'Gaspar Mew', '(960) 1051185', '487 Northland Hill'),
('cwhitseyk@ustream.tv', 'Clay Whitsey', '(300) 1460818', '3 Prairieview Avenue'),
('gpettegrel@wix.com', 'Gail Pettegre', '(395) 1611101', '82 Gateway Point'),
('iswaddlem@hao123.com', 'Iain Swaddle', '(571) 9183178', '29213 Union Drive'),
('wyitzhakofn@youtube.com', 'Willabella Yitzhakof', '(992) 4452213', '8362 Gateway Center'),
('vloreko@storify.com', 'Vivienne Lorek', '(930) 4723520', '72784 Larry Crossing'),
('dillistonp@smh.com.au', 'Damita Illiston', '(666) 8719182', '09 Main Trail'),
('aspragueq@yandex.ru', 'Allene Sprague', '(226) 7067839', '1229 Spenser Place'),
('rnozzoliniir@usgs.gov', 'Rici Nozzolinii', '(253) 5862648', '57 Redwing Street'),
('kormans@sohu.com', 'Kurtis Orman', '(782) 4785923', '0 Larry Place'),
('sdressellt@behance.net', 'Sydney Dressell', '(988) 3209390', '72717 Grim Trail'),
('sespinazou@ucla.edu', 'Sal Espinazo', '(693) 6817848', '863 Clove Point'),
('mgiacominiv@amazon.de', 'Masha Giacomini', '(946) 5801764', '67960 Forest Dale Hill'),
('soscroftw@smugmug.com', 'Sammy Oscroft', '(268) 9627837', '307 Mcbride Crossing'),
('tfarnallx@prlog.org', 'Torrey Farnall', '(987) 3913918', '95511 Calypso Lane'),
('abalmay@yahoo.com', 'Adriaens Balma', '(837) 2711910', '1798 School Alley'),
('krossz@drupal.org', 'Kipper Ross', '(531) 1160005', '23 Roxbury Lane'),
('mbeaten10@utexas.edu', 'Merill Beaten', '(491) 3746403', '54 Lien Trail'),
('pmachent11@t.co', 'Pat Machent', '(111) 7309571', '12 Ridge Oak Terrace'),
('jmacduffie12@eepurl.com', 'Joyann MacDuffie', '(722) 3543634', '12 Spenser Pass'),
('wten13@google.de', 'Walton Ten Broek', '(727) 4821522', '2 Pine View Park'),
('sdabell14@networksolutions.com', 'Selby Dabell', '(933) 3542108', '048 Hovde Place'),
('fpleasaunce15@gov.uk', 'Fred Pleasaunce', '(132) 1216018', '8 Knutson Drive'),
('acorragan16@admin.ch', 'Anselma Corragan', '(758) 9406460', '96 Red Cloud Way'),
('sschofield17@prnewswire.com', 'Sisile Schofield', '(627) 1722579', '1 Myrtle Road'),
('omorillas18@youtube.com', 'Olive Morillas', '(130) 4187610', '9569 Ronald Regan Avenue'),
('abiaggi19@cbslocal.com', 'Adena Biaggi', '(444) 2188080', '36 Elgar Way'),
('cpeterken1a@symantec.com', 'Cinderella Peterken', '(287) 1923619', '826 Dapin Pass'),
('cmclukie1b@salon.com', 'Clarke McLukie', '(315) 7924147', '261 Cordelia Terrace'),
('vremon1c@mail.ru', 'Vonny Remon', '(363) 4197326', '9 Schurz Junction'),
('emanach1d@booking.com', 'Evangelina Manach', '(173) 7592909', '1189 Morrow Plaza')

drop table if exists `Order`;

create table if not exists `Order`(
	orderId INT AUTO_INCREMENT,
	customerId VARCHAR(40),
	`status` VARCHAR(40),
	PRIMARY KEY (orderId),
	FOREIGN KEY (customerId) REFERENCES Customer(customerId)
);

insert into `Order` (orderId, customerId, `status`) values
(1, 'emanach1d@booking.com', 'Paid'),
(2, 'vremon1c@mail.ru', 'Pending'),
(3, 'omorillas18@youtube.com', 'Paid'),
(4, 'emanach1d@booking.com', 'Cancelled')


drop table if exists OrderItem;

create table OrderItem (
    orderId INT,
    itemId VARCHAR(40),
    quantity INT,
    PRIMARY KEY (orderId, itemId),
    FOREIGN KEY (orderId) REFERENCES `Order`(orderId),
    FOREIGN KEY (itemId) REFERENCES Item(itemId)
);

drop table if exists ShopItem;

create table ShopItem (
    shopId VARCHAR(40),
    itemId VARCHAR(40),
    PRIMARY KEY (shopId, itemId),
    FOREIGN KEY (shopId) REFERENCES `Shop`(shopId),
    FOREIGN KEY (itemId) REFERENCES Item(itemId)
);

insert into ShopItem (shopId, itemId) values
('93d773fe-4c26-46f4-a7dc-c767fbbd266e', '431c7779-4cd6-44f6-ae1c-da80a13fe633'),
('93d773fe-4c26-46f4-a7dc-c767fbbd266e', '7d49c255-b254-4734-9298-4c38c6c475c2'),
('93d773fe-4c26-46f4-a7dc-c767fbbd266e', 'd11a919d-bc55-4c12-bf1f-919814ca2a4d'),
('2ef1ce37-30f3-4a33-8961-5798cb8e3351', '431c7779-4cd6-44f6-ae1c-da80a13fe633')