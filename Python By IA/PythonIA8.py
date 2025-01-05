from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta  # Necesita instalación previa con pip

# Obtener fecha y hora actual
Hora_Fecha_Actual = datetime.now()
print("Fecha y hora actual:", Hora_Fecha_Actual)

# Extraer solo la fecha
Solo_Fecha = Hora_Fecha_Actual.date()
print("Solo la fecha:", Solo_Fecha)

# Calcular la fecha dentro de 7 días
Fecha_7Dias = Hora_Fecha_Actual + timedelta(days=7)
print("Fecha dentro de 7 días:", Fecha_7Dias.date())

# Calcular una fecha específica (cumpleaños) y retroceder un año
Cumpleaños = datetime(2025, 10, 28)
Retro = Cumpleaños - relativedelta(years=1)
print("Un año antes del cumpleaños:", Retro.date())

























