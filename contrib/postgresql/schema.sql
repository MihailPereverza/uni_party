-- Создание таблицы users
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY, -- изменено с user_id на id
    tg_id BIGINT UNIQUE NOT NULL, -- Telegram ID
    username VARCHAR(255), -- Username в Telegram
    full_name VARCHAR(255), -- Полное имя пользователя
    is_admin BOOLEAN DEFAULT FALSE, -- Флаг администратора
    created_at TIMESTAMP DEFAULT NOW()
);

-- Создание таблицы events
CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY, -- изменено с event_id на id
    title VARCHAR(255) NOT NULL, -- Название мероприятия
    description TEXT, -- Описание мероприятия
    start_time TIMESTAMP NOT NULL, -- Время начала
    end_time TIMESTAMP, -- Время окончания
    created_at TIMESTAMP DEFAULT NOW(),
    created_by INTEGER REFERENCES users(id) ON DELETE SET NULL -- Создатель мероприятия
);

-- Создание таблицы event_participants
CREATE TABLE IF NOT EXISTS event_participants (
    id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES events(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    registered_at TIMESTAMP DEFAULT NOW(), -- Время записи
    UNIQUE(event_id, user_id) -- Уникальная пара участник/мероприятие
);

-- Создание таблицы quizzes
CREATE TABLE IF NOT EXISTS quizzes (
    id SERIAL PRIMARY KEY, -- изменено с quiz_id на id
    event_id INTEGER REFERENCES events(id) ON DELETE CASCADE, -- Привязка к мероприятию
    title VARCHAR(255) NOT NULL, -- Название квиза
    url VARCHAR(255) NOT NULL, -- URL квиза
    created_at TIMESTAMP DEFAULT NOW(),
    created_by INTEGER REFERENCES users(id) ON DELETE SET NULL -- Создатель квиза
);

-- Создание таблицы quiz_results
CREATE TABLE IF NOT EXISTS quiz_results (
    id SERIAL PRIMARY KEY, -- изменено с result_id на id
    quiz_id INTEGER REFERENCES quizzes(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    score INTEGER, -- Результат пользователя
    completed_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(quiz_id, user_id) -- Уникальная пара квиз/пользователь
);

-- Создание таблицы notifications
CREATE TABLE IF NOT EXISTS notifications (
    id SERIAL PRIMARY KEY, -- изменено с notification_id на id
    event_id INTEGER REFERENCES events(id) ON DELETE CASCADE, -- Для какого мероприятия
    message TEXT NOT NULL, -- Текст уведомления
    created_at TIMESTAMP DEFAULT NOW(),
    sent_by INTEGER REFERENCES users(id) ON DELETE SET NULL -- Отправитель уведомления
);

-- Создание таблицы schedules
CREATE TABLE IF NOT EXISTS schedules (
    id SERIAL PRIMARY KEY, -- изменено с schedule_id на id
    event_id INTEGER REFERENCES events(id) ON DELETE CASCADE, -- Для какого мероприятия
    schedule_md TEXT NOT NULL, -- Расписание мероприятия в формате Markdown
    added_at TIMESTAMP DEFAULT NOW() -- Время добавления в расписание
);
