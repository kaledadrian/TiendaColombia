-- Insertar Usuario
INSERT INTO actores (nombre, email, password, rol, fecha_registro, activo) VALUES
('Carlos Rodríguez', 'carlos@empresa.com', 'pbkdf2_sha256$600000$7YJ5tTYX7ZKs0j2f9XkL3d$8JgkL8KJp2xYs6tR4vW9mN2qP5rT3bF7hJkL2mN4pQ=', 'admin', NOW(), 1);

-- Insertar Usuarios Regulares
INSERT INTO actores (nombre, email, password, rol, fecha_registro, activo) VALUES
('María González', 'maria@email.com', 'pbkdf2_sha256$600000$8Zk6uUY8YaLt3kG0gYmL4e$9LkM9KqR3yZt7uS5wX0nO3rS6uT4cG8iKlM3nO5pR=', 'usuario', NOW(), 1),
('Juan Pérez', 'juan@email.com', 'pbkdf2_sha256$600000$8Zk6uUY8YaLt3kG0gYmL4e$9LkM9KqR3yZt7uS5wX0nO3rS6uT4cG8iKlM3nO5pR=', 'usuario', NOW(), 1),
('Ana Martínez', 'ana@email.com', 'pbkdf2_sha256$600000$8Zk6uUY8YaLt3kG0gYmL4e$9LkM9KqR3yZt7uS5wX0nO3rS6uT4cG8iKlM3nO5pR=', 'usuario', NOW(), 1),
('Pedro Sánchez', 'pedro@email.com', 'pbkdf2_sha256$600000$8Zk6uUY8YaLt3kG0gYmL4e$9LkM9KqR3yZt7uS5wX0nO3rS6uT4cG8iKlM3nO5pR=', 'usuario', NOW(), 1),
('Luisa Fernández', 'luisa@email.com', 'pbkdf2_sha256$600000$8Zk6uUY8YaLt3kG0gYmL4e$9LkM9KqR3yZt7uS5wX0nO3rS6uT4cG8iKlM3nO5pR=', 'usuario', NOW(), 1),
('Andrés López', 'andres@email.com', 'pbkdf2_sha256$600000$8Zk6uUY8YaLt3kG0gYmL4e$9LkM9KqR3yZt7uS5wX0nO3rS6uT4cG8iKlM3nO5pR=', 'usuario', NOW(), 1);

-- Insertar métodos de pago
INSERT INTO metodos_pago (nombre, descripcion) VALUES
('Efectivo', 'Pago en efectivo en COP'),
('Nequi', 'Pago por Nequi app'),
('Daviplata', 'Pago por Daviplata'),
('Tarjeta Débito', 'Pago con tarjeta débito'),
('Tarjeta Crédito', 'Pago con tarjeta de crédito'),
('Transferencia', 'Transferencia bancaria'),
('PSE', 'Pago por PSE en línea'),
('RappiPay', 'Pago con RappiPay');

-- Insertar categorías
INSERT INTO categorias (nombre, descripcion, color, icono, fecha_creacion) VALUES
('Alimentación', 'Comida, mercado, restaurantes', '#28a745', 'bi-cart', NOW()),
('Transporte', 'Taxi, bus, TransMilenio, gasolina', '#17a2b8', 'bi-bus-front', NOW()),
('Vivienda', 'Arriendo, servicios públicos, mantenimiento', '#007bff', 'bi-house', NOW()),
('Salud', 'Medicinas, consultas médicas, EPS', '#dc3545', 'bi-heart', NOW()),
('Educación', 'Matrículas, cursos, libros', '#fd7e14', 'bi-book', NOW()),
('Entretenimiento', 'Cine, streaming, salidas', '#6f42c1', 'bi-tv', NOW()),
('Ropa', 'Vestimenta, calzado, accesorios', '#e83e8c', 'bi-bag', NOW()),
('Tecnología', 'Celular, internet, equipos', '#20c997', 'bi-phone', NOW());


-- GASTOS PARA MARZO 2026
-- Usuario María González (ID 2)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, fecha_registro) VALUES
('Mercado Mensual Marzo', 'Compra mercado éxito', 380000, '2026-03-05', 1, 1, 2, NOW()),
('Arriendo Marzo', 'Pago arriendo', 1500000, '2026-03-10', 3, 4, 2, NOW()),
('Transporte Marzo', 'Recarga TransMilenio', 90000, '2026-03-15', 2, 2, 2, NOW()),
('Salud Marzo', 'Consulta médica', 150000, '2026-03-20', 4, 1, 2, NOW()),
('Entretenimiento Marzo', 'Cine y comida', 180000, '2026-03-25', 6, 5, 2, NOW());

-- Usuario Juan Pérez (ID 3)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, fecha_registro) VALUES
('Gasolina Marzo', 'Tanque lleno', 180000, '2026-03-03', 2, 1, 3, NOW()),
('Mercado Marzo', 'Compra D1', 150000, '2026-03-08', 1, 3, 3, NOW()),
('Internet Marzo', 'Pago Claro', 95000, '2026-03-12', 8, 4, 3, NOW()),
('Luz Marzo', 'Servicio energía', 120000, '2026-03-18', 3, 2, 3, NOW()),
('Gimnasio Marzo', 'Mensualidad', 120000, '2026-03-22', 6, 4, 3, NOW());

-- Usuario Ana Martínez (ID 4)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, fecha_registro) VALUES
('Ropa Marzo', 'Compra zapatos', 250000, '2026-03-06', 7, 5, 4, NOW()),
('Uber Marzo', 'Viajes trabajo', 130000, '2026-03-11', 2, 3, 4, NOW()),
('Mercado Marzo', 'Olímpica', 300000, '2026-03-16', 1, 1, 4, NOW()),
('Streaming Marzo', 'Netflix y Spotify', 70000, '2026-03-21', 6, 5, 4, NOW()),
('Salud Marzo', 'Farmacia', 85000, '2026-03-26', 4, 1, 4, NOW());

-- Usuario Pedro Sánchez (ID 5)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, fecha_registro) VALUES
('Educación Marzo', 'Cursos online', 350000, '2026-03-04', 5, 4, 5, NOW()),
('Transporte Marzo', 'SITP buses', 70000, '2026-03-09', 2, 2, 5, NOW()),
('Comida Marzo', 'Restaurantes', 200000, '2026-03-14', 1, 5, 5, NOW()),
('Tecnología Marzo', 'Accesorios', 150000, '2026-03-19', 8, 4, 5, NOW()),
('Entretenimiento Marzo', 'Videojuegos', 120000, '2026-03-24', 6, 2, 5, NOW());

-- GASTOS PARA ABRIL 2026

-- Usuario María González (ID 2)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, fecha_registro) VALUES
('Mercado Abril', 'Compra mercado', 420000, '2026-04-05', 1, 1, 2, NOW()),
('Arriendo Abril', 'Pago arriendo', 1500000, '2026-04-10', 3, 4, 2, NOW()),
('Transporte Abril', 'Taxi y TransMi', 110000, '2026-04-15', 2, 3, 2, NOW()),
('Ropa Abril', 'Ropa deportiva', 220000, '2026-04-20', 7, 5, 2, NOW()),
('Salud Abril', 'Odontología', 250000, '2026-04-25', 4, 1, 2, NOW());

-- Usuario Juan Pérez (ID 3)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, fecha_registro) VALUES
('Gasolina Abril', 'Tanque lleno', 190000, '2026-04-03', 2, 1, 3, NOW()),
('Mercado Abril', 'Compra Ara', 130000, '2026-04-08', 1, 1, 3, NOW()),
('Servicios Abril', 'Agua y gas', 200000, '2026-04-13', 3, 2, 3, NOW()),
('Tecnología Abril', 'Celular nuevo', 800000, '2026-04-18', 8, 5, 3, NOW()),
('Entretenimiento Abril', 'Concierto', 250000, '2026-04-23', 6, 4, 3, NOW());

-- Usuario Ana Martínez (ID 4)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, fecha_registro) VALUES
('Ropa Abril', 'Jeans y blusas', 300000, '2026-04-06', 7, 5, 4, NOW()),
('Transporte Abril', 'Uber y Didi', 140000, '2026-04-11', 2, 3, 4, NOW()),
('Mercado Abril', 'Carulla', 350000, '2026-04-16', 1, 4, 4, NOW()),
('Salud Abril', 'Medicinas', 95000, '2026-04-21', 4, 1, 4, NOW()),
('Gimnasio Abril', 'Mensualidad', 120000, '2026-04-26', 6, 2, 4, NOW());

-- Usuario Pedro Sánchez (ID 5)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, fecha_registro) VALUES
('Libros Abril', 'Libros universitarios', 400000, '2026-04-04', 5, 4, 5, NOW()),
('Transporte Abril', 'Recarga SITP', 80000, '2026-04-09', 2, 2, 5, NOW()),
('Comida Abril', 'Domicilios', 180000, '2026-04-14', 1, 8, 5, NOW()),
('Entretenimiento Abril', 'Cine', 100000, '2026-04-19', 6, 5, 5, NOW()),
('Mascotas Abril', 'Alimento perro', 120000, '2026-04-24', 4, 1, 5, NOW());


--  GASTOS PARA MAYO 
-- GASTOS PARA USUARIO María González (ID asumido = 2)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, comprobante, fecha_registro) VALUES
('Mercado Semanal', 'Compra en Éxito - alimentos básicos', 350000, '2025-05-01', 1, 1, 2, NULL, NOW()),
('Pago Arriendo', 'Arriendo apartamento Mayo', 1500000, '2025-05-05', 3, 4, 2, NULL, NOW()),
('Recarga TransMilenio', 'Recarga tarjeta personal', 80000, '2025-05-07', 2, 2, 2, NULL, NOW()),
('Cena Restaurante', 'Cena con amigos en Crepes & Waffles', 180000, '2025-05-10', 1, 5, 2, NULL, NOW()),
('Gimnasio', 'Mensualidad Mayo - Smart Fit', 120000, '2025-05-12', 6, 4, 2, NULL, NOW()),
('Internet', 'Pago Claro 200 megas', 95000, '2025-05-15', 8, 3, 2, NULL, NOW()),
('Medicamentos', 'Farmacia - medicamentos receta', 65000, '2025-05-18', 4, 1, 2, NULL, NOW()),
('Peluquería', 'Corte y tintura', 120000, '2025-05-20', 7, 2, 2, NULL, NOW());

-- GASTOS PARA USUARIO Juan Pérez (ID asumido = 3)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, comprobante, fecha_registro) VALUES
('Gasolina', 'Tanque lleno carro', 150000, '2025-05-02', 2, 1, 3, NULL, NOW()),
('Mercado D1', 'Compra mercado D1', 120000, '2025-05-04', 1, 3, 3, NULL, NOW()),
('Netflix', 'Subscripción mensual', 45000, '2025-05-06', 6, 5, 3, NULL, NOW()),
('Servicio Luz', 'Factura de energía Mayo', 110000, '2025-05-09', 3, 2, 3, NULL, NOW()),
('Celular', 'Pago plan Movistar', 55000, '2025-05-11', 8, 4, 3, NULL, NOW()),
('Zapatos', 'Compra zapatos deportivos', 280000, '2025-05-14', 7, 5, 3, NULL, NOW()),
('Veterinaria', 'Vacunas perro', 180000, '2025-05-17', 4, 1, 3, NULL, NOW()),
('Cine', 'Película con amigos', 85000, '2025-05-19', 6, 2, 3, NULL, NOW()),
('Paseo Dominical', 'Almuerzo familiar', 210000, '2025-05-20', 1, 4, 3, NULL, NOW());

-- GASTOS PARA USUARIO Ana Martínez (ID asumido = 4)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, comprobante, fecha_registro) VALUES
('Uber Viajes', 'Viajes al trabajo semana', 120000, '2025-05-03', 2, 3, 4, NULL, NOW()),
('Zapatos', 'Zapatos para oficina', 210000, '2025-05-05', 7, 5, 4, NULL, NOW()),
('Spotify', 'Subscripción premium', 25000, '2025-05-07', 6, 4, 4, NULL, NOW()),
('Mercado', 'Mercado Olímpica', 280000, '2025-05-09', 1, 1, 4, NULL, NOW()),
('Agua', 'Servicio acueducto', 85000, '2025-05-12', 3, 2, 4, NULL, NOW()),
('Ropa Deportiva', 'Ropa para gimnasio', 180000, '2025-05-15', 7, 5, 4, NULL, NOW()),
('Consulta Médica', 'Medicina general', 120000, '2025-05-18', 4, 1, 4, NULL, NOW()),
('Salida Amigas', 'Brunch domingo', 150000, '2025-05-20', 1, 3, 4, NULL, NOW());

-- GASTOS PARA USUARIO Pedro Sánchez (ID asumido = 5)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, comprobante, fecha_registro) VALUES
('Libros', 'Compra libros universitarios', 320000, '2025-05-01', 5, 4, 5, NULL, NOW()),
('Mercado', 'Mercado Ara', 95000, '2025-05-04', 1, 1, 5, NULL, NOW()),
('TransMilenio', 'Recarga tarjeta', 60000, '2025-05-06', 2, 2, 5, NULL, NOW()),
('Gas', 'Servicio gas domiciliario', 75000, '2025-05-08', 3, 1, 5, NULL, NOW()),
('Platzi', 'Subscripción curso', 95000, '2025-05-10', 5, 5, 5, NULL, NOW()),
('Comida Rápida', 'McDonald\'s', 55000, '2025-05-13', 1, 2, 5, NULL, NOW()),
('Camisa', 'Ropa casual', 120000, '2025-05-16', 7, 4, 5, NULL, NOW()),
('Criptomonedas', 'Inversión', 500000, '2025-05-19', 6, 7, 5, NULL, NOW()),
('Farmacia', 'Medicamentos', 45000, '2025-05-20', 4, 1, 5, NULL, NOW());

-- GASTOS PARA USUARIO Luisa Fernández (ID asumido = 6)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, comprobante, fecha_registro) VALUES
('Domicilio Rappi', 'Comida a domicilio', 85000, '2025-05-02', 1, 8, 6, NULL, NOW()),
('Mascotas', 'Alimento perro', 110000, '2025-05-05', 4, 1, 6, NULL, NOW()),
('Peajes', 'Viaje fuera de Bogotá', 70000, '2025-05-07', 2, 1, 6, NULL, NOW()),
('Netflix', 'Subscripción', 45000, '2025-05-09', 6, 5, 6, NULL, NOW()),
('Salón Belleza', 'Manicure y pedicure', 90000, '2025-05-11', 7, 2, 6, NULL, NOW()),
('Mercado', 'Mercado Justo & Bueno', 150000, '2025-05-14', 1, 1, 6, NULL, NOW()),
('Internet', 'Pago Claro', 85000, '2025-05-16', 8, 3, 6, NULL, NOW()),
('Regalo', 'Regalo cumpleaños hermana', 250000, '2025-05-18', 6, 4, 6, NULL, NOW()),
('Gimnasio', 'Mensualidad', 100000, '2025-05-20', 6, 2, 6, NULL, NOW());

-- GASTOS PARA USUARIO Andrés López (ID asumido = 7)
INSERT INTO gastos (titulo, descripcion, monto, fecha, categoria_id, metodo_pago_id, usuario_id, comprobante, fecha_registro) VALUES
('Herramientas', 'Compra ferretería', 180000, '2025-05-03', 3, 1, 7, NULL, NOW()),
('Gasolina', 'Tanque carro', 160000, '2025-05-06', 2, 4, 7, NULL, NOW()),
('Mercado', 'Mercado Carulla', 300000, '2025-05-08', 1, 5, 7, NULL, NOW()),
('Prime Video', 'Subscripción', 35000, '2025-05-10', 6, 5, 7, NULL, NOW()),
('Farmacia', 'Medicamentos', 70000, '2025-05-12', 4, 1, 7, NULL, NOW()),
('Ropa', 'Jeans y camisetas', 250000, '2025-05-15', 7, 4, 7, NULL, NOW()),
('Celular', 'Pago plan Tigo', 65000, '2025-05-17', 8, 2, 7, NULL, NOW()),
('Cena Aniversario', 'Cena romántica', 320000, '2025-05-19', 1, 5, 7, NULL, NOW()),
('Servicio Luz', 'Factura energía', 130000, '2025-05-20', 3, 1, 7, NULL, NOW());