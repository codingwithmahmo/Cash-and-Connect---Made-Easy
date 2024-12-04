CREATE TABLE IF NOT EXISTS adminDetails (
    username TEXT PRIMARY KEY,
    password TEXT
);

-- Insert initial data
INSERT OR IGNORE INTO adminDetails (username, password) VALUES
('mahmood', 'khan'),
('mehboob', 'rasheed'),
('uzair', 'baig');

