from typing import Literal

Area = Literal[
    "km2", "ha", "are", "m2", "dm2", "cm2", "mm2", "micrometro2", "acre", "milla2", "yd2", "ft2", "in2", "rd2", "qing", "chi2", "cun2", "gongli2"]
IMC_Peso = Literal["kg", "lb"]
IMC_Altura = Literal["cm", "m", "ft", "in"]
Datos = Literal["B", "KB", "MB", "GB", "TB", "PB"]
Longitud = Literal[
    "km", "m", "dm", "cm", "mm", "micrometro", "nanometro", "picometro", "nmi", "mi", "fur", "ftm", "yd", "ft", "in", "gongli", "li", "chi", "cun", "fen", "lii", "parsec", "distancia-lunar", "unidad-astronomica", "anno-luz"]
Masa = Literal["t", "kg", "g", "mg", "microgramo", "quintal", "lb", "oz", "carat", "grano"]
Sistema_Numerico = Literal["BIN", "OCT", "DEC", "HEX"]
Velocidad = Literal["c", "Ma", "m-s", "km-h", "km-s", "kn", "mph", "fps", "ips"]
Temperatura = Literal["celsius", "fahrenheit", "kelvin", "rankine", "reaumur"]
Tiempo = Literal["anno", "semana", "dia", "hora", "minuto", "segundo", "milisegundo", "microsegundo", "picosegundo"]
Volumen = Literal["m3", "dm3", "cm3", "mm3", "hl", "l", "dl", "cl", "ml", "ft3", "in3", "yd3", "af3"]
Angulo = Literal["radianes", "grados"]
Divisa = Literal[
    'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD',
    'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD',
    'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP',
    'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD',
    'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD',
    'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD',
    'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT',
    'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR',
    'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB',
    'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STN',
    'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH',
    'UGX', 'USD', 'USDC', 'USDT', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU',
    'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']
