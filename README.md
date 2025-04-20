# 🏗️ Construction Project Management - Odoo 17

Este módulo personalizado para **Odoo 17** permite gestionar proyectos del sector de construcción con seguimiento de tareas, generación automática de facturas al 50% de avance y visualización del progreso del proyecto.

---

## 📦 Características Principales

- Modelo personalizado `construction.project` con:
  - Nombre del proyecto
  - Fechas de inicio y fin
  - Presupuesto
  - Cliente (Many2one con `res.partner`)
  - Progreso calculado automáticamente en función de tareas completadas
- Relación One2many con `construction.task`, que incluye:
  - Nombre de la tarea
  - Estado (Pendiente, En Progreso, Completada)
  - Fecha límite
  - Responsable (usuario asignado)
- Validación de fechas: no se permite que la fecha de fin sea anterior a la de inicio.
- Factura generada automáticamente al alcanzar el 50% de avance.
- Vista con gráfico de progreso usando `widget="progressbar"`.
- API REST para consultar el estado del proyecto:  
  `POST /api/project/status/<id>`

---

## 🧠 Justificación Técnica

- Uso de `@api.depends` para el cálculo reactivo del progreso.
- `@api.constrains` para validar las fechas de inicio y fin.
- Generación de facturas con el modelo `account.move`.
- Controlador REST implementado con `auth='public'` y acceso controlado mediante `sudo()` (configurable).

---


