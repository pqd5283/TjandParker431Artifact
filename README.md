# TjandParker431Artifact


CREATE TABLE Contract(
ContractID INT PRIMARY KEY,
StartTime DATETIME,
EndTime DATETIME,
Salary DECIMAL(10,2),
Type VARCHAR(255));


CREATE TABLE Player (
PlayerID INT Primary Key,
Fname VARCHAR(255),
Lname VARCHAR (255));

CREATE TABLE QB(
PlayerID INT PRIMARY KEY,
Depth INT,
CompletionPercentage DECIMAL(2,2),
PassingYards INT,
QBR DECIMAL(3,1),
TDs INT,
FOREIGN KEY(PlayerID) REFERENCES Player(PlayerID)
ON UPDATE RESTRICT ON DELETE CASCADE);

CREATE TABLE RB(
PlayerID INT PRIMARY KEY,
Depth INT,
YardsPerCarry DECIMAL(3,1),
RushingYards INT,
Attempts INT,
TDs INT,
FOREIGN KEY(PlayerID) REFERENCES Player(PlayerID)
ON UPDATE RESTRICT ON DELETE CASCADE);

CREATE TABLE WR(
PlayerID INT PRIMARY KEY,
Depth INT,
ReceivingYards INT,
Targets INT,
YardsPerReception DECIMAL(3,1),
TDs INT,
FOREIGN KEY(PlayerID) REFERENCES Player(PlayerID)
ON UPDATE RESTRICT ON DELETE CASCADE);

CREATE TABLE Defense(
PlayerID INT PRIMARY KEY,
Depth INT,
Position INT,
Tackles INT,
Sacks INT,
Ints INT,
Fumbles INT,
FOREIGN KEY(PlayerID) REFERENCES Player(PlayerID)
ON UPDATE RESTRICT ON DELETE CASCADE);


CREATE TABLE Coach(
CoachID INT PRIMARY KEY,
Fname VARCHAR(255),
Lname VARCHAR(255),
Supervisor INT,
Title VARCHAR(255),
ContractID INT,
FOREIGN KEY(ContractID) REFERENCES Contract(ContractID)
ON UPDATE RESTRICT ON DELETE CASCADE,
FOREIGN KEY(Supervisor) REFERENCES Coach(CoachID)
ON UPDATE RESTRICT ON DELETE CASCADE);


CREATE TABLE CurrentPlayer(
PlayerID INT PRIMARY KEY,
ContractID INT,
CoachID INT,
Number INT,
UNIQUE(Number),
FOREIGN KEY(PlayerID) REFERENCES Player(PlayerID)
ON UPDATE RESTRICT ON DELETE CASCADE,
FOREIGN KEY(ContractID) REFERENCES Contract(ContractID)
ON UPDATE RESTRICT ON DELETE CASCADE,
FOREIGN KEY(CoachID) REFERENCES Coach(CoachID)
ON UPDATE RESTRICT ON DELETE CASCADE);

CREATE TABLE TradeTarget(
PlayerID INT PRIMARY KEY,
Fname VARCHAR(255),
Lname VARCHAR(255),
Team VARCHAR(255),
FOREIGN KEY(PlayerID) REFERENCES Player(PlayerID)
ON UPDATE RESTRICT ON DELETE CASCADE);

CREATE TABLE TradeProposal(
TradeID INT PRIMARY KEY,
OldPlayer INT,
NewPlayer INT,
Status VARCHAR(255),
AdditionalOffers VARCHAR(255),
FOREIGN KEY(OldPlayer) REFERENCES CurrentPlayer(PlayerID)
ON UPDATE RESTRICT ON DELETE CASCADE,
FOREIGN KEY(NewPlayer) REFERENCES TradeTarget(PlayerID)
ON UPDATE RESTRICT ON DELETE CASCADE);


-- Insert entries into Player
INSERT INTO Player (PlayerID, Fname, Lname) VALUES 
(1, 'Russel', 'Wilson'),
(2, 'Justin', 'Fields'),
(3, 'Kyle', 'Allen'),
(4, 'Najee', 'Harris'),
(5, 'Jalen', 'Warren'),
(6, 'Cordale', 'Patterson'),
(7, 'George', 'Pickens'),
(8, 'Mike', 'Williams'),
(9, 'Van', 'Jefferson'),
(10, 'Tj', 'Watt'),
(11, 'Alex', 'Highsmith'),
(12, 'Patrick', 'Queen'),
(13, 'Josh', 'Allen'),
(14, 'Justin', 'Jefferson'),
(15, 'Saquon', 'Barkley'),
(16, 'Miles', 'Garret');


-- Insert entries into QB
INSERT INTO QB (PlayerID, Depth, CompletionPercentage, PassingYards, QBR, TDs) VALUES 
(1, 1, .68, 3500, 95.3, 25),
(2, 2, .64, 2800, 88.1, 20),
(3, 3, .62, 2200, 79.5, 15),
(13, NULL, .58, 1500, 70.8, 10);


-- Insert entries into RB
INSERT INTO RB (PlayerID, Depth, YardsPerCarry, RushingYards, Attempts, TDs) VALUES 
(4, 1, 4.8, 1200, 250, 10),
(5, 2, 5.1, 1050, 200, 12),
(6, 3, 3.9, 850, 220, 8),
(14, NULL, 4.2, 900, 210, 9);

-- Insert entries into WR
INSERT INTO WR (PlayerID, Depth, ReceivingYards, Targets, YardsPerReception, TDs) VALUES 
(7, 1, 1300, 120, 10.8, 10),
(8, 2, 1100, 95, 11.5, 8),
(9, 3, 950, 80, 12.0, 6),
(15, NULL, 750, 70, 10.7, 4);


-- Insert entries into Defense
INSERT INTO Defense (PlayerID, Depth, Position, Tackles, Sacks, Ints, Fumbles) VALUES 
(10, 1, "Linebacker", 85, 10, 5, 2),
(11, 2, "Corner", 72, 8, 3, 1),
(12, 3, "Safety", 90, 12, 6, 3),
(16, NULL, "DLine", 80, 7, 4, 2);

-- Insert entries into Contract
INSERT INTO Contract (ContractID, StartTime, EndTime, Salary, Type) VALUES 
(1, '2024-01-01', '2026-12-31', 1000000.00, 'Player'),
(2, '2024-01-01', '2025-12-31', 800000.00, 'Player'),
(3, '2024-01-01', '2027-12-31', 1200000.00, 'Player'),
(4, '2024-01-01', '2026-06-30', 950000.00, 'Player'),
(5, '2024-01-01', '2025-12-31', 700000.00, 'Player'),
(6, '2024-01-01', '2028-12-31', 1500000.00, 'Player'),
(7, '2024-01-01', '2026-12-31', 1100000.00, 'Player'),
(8, '2024-01-01', '2025-06-30', 850000.00, 'Player'),
(9, '2024-01-01', '2027-03-29', 1400000.00, 'Player'),
(10, '2024-01-01', '2029-12-31', 1300000.00, 'Player'),
(11, '2024-01-01', '2025-08-12', 490000.00, 'Coach'),
(12, '2024-01-01', '2028-7-3', 1000000.00, 'Coach'),
(13, '2024-01-01', '2034-05-24', 4500000.00, 'Coach'),
(14, '2024-01-01', '2026-04-17', 9800000.00, 'Coach'),
(15, '2024-01-01', '2029-07-12', 380000.00, 'Coach'),
(16, '2024-01-01', '2024-12-8', 890000.00, 'Coach');

-- Insert entries into Coach
INSERT INTO Coach (CoachID, Fname, Lname, Supervisor, Title, ContractID) VALUES 
(1, 'Alex', 'Brown', NULL, 'Head Coach', 11),
(2, 'Taylor', 'Green', 1, 'Offensive Coordinator', 12),
(3, 'Jordan', 'Lee', 1, 'Defensive Coordinator', 13),
(4, 'Morgan', 'Kim', 2, 'QB Coach', 14),
(5, 'Drew', 'White', 2, 'WR Coach', 15),
(6, 'Riley', 'Black', 2, 'RB Coach', 16);


-- Insert entries into CurrentPlayer
INSERT INTO CurrentPlayer (PlayerID, ContractID, CoachID, Number) VALUES 
(1, 1, 1, 7),
(2, 2, 1, 12),
(3, 3, 1, 84),
(4, 4, 2, 52),
(5, 5, 2, 33),
(6, 6, 2, 21),
(7, 7, 3, 99),
(8, 8, 3, 11),
(9, 9, 3, 27),
(10, 10, 4, 54),
(11, 11, 4, 48),
(12, 12, 4, 83);

-- Insert entries into TradeTarget
INSERT INTO TradeTarget (PlayerID, Fname, Lname, Team) VALUES 
(13, 'Josh', 'Allen', 'Bills'),
(14, 'Justin', 'Jefferson', 'Vikings'),
(15, 'Saquon', 'Barkley', 'Eagles'),
(16, 'Miles', 'Garret', 'Browns');


-- Insert entries into TradeProposal
INSERT INTO TradeProposal (TradeID, OldPlayer, NewPlayer, Status, AdditionalOffers) VALUES 
(1, 1, 13, 'Pending', 'None'),
(2, 4, 14, 'Pending', 'None'),
(3, 9, 15, 'Pending', 'Draft Picks'),
(4, 12, 16, 'Pending', 'Draft Picks');


