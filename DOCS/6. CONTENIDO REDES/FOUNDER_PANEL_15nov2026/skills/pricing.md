# Precio de «Arreglo de Caja» (15 nov 2026)

**Aviso.** Panel simulado, perfil escrito por Claude: el rango es una hipótesis, no una prueba. (La curva dice «$»; son euros.)

## 1. Qué dicen las fuentes

| Fuente | Dato | Lectura |
| --- | --- | --- |
| Panel simulado | Rango 31 a 131 €; menor resistencia 40 €; indiferencia 70 € | 99 € está dentro, cerca del techo: a 13 de 20 ya les parece «caro», a nadie «demasiado caro» |
| Panel simulado | 198 y 249 € «demasiado caro» para 13 y 16 de 20 | Los planes grandes quedan fuera del rango |
| Competidores (enlaces en competitors.md) | Gestoría 29,95 a 65 €/mes; Declarando Premium 99,90 €/mes; cursos 61 a 520 € | 99 € único es mes y medio de gestoría; nadie publica precio cerrado por arreglar cobros |

## 2. Margen: falta el dato, aquí va la fórmula

No hay coste por hora ni horas por síntoma; no calculo ningún margen. Faltan:
- **c**: coste por hora del consultor, con cargas.
- **h**: horas de consultor por síntoma (revisión, número final, hoja del gestor).
- **q**: parte de clientes que mejora a la primera; el resto cuesta **h_extra** por la garantía.
- **t**: comisión de Stripe; **I**: costes fijos mensuales (FALTA); **N**: tratamientos al mes.

**Precio mínimo de equilibrio:** P_min = c × (h + (1 − q) × h_extra) / (1 − t) + I / N

**En dos pagos (39 + 60):** el primer paso sale a cuenta si c × h_paso1 ≤ 39 × (1 − t). El total, si 39 + q × 60 ≥ P_min. Sin q real, el segundo pago no cuenta como ingreso.

## 3. Escalera (precios ya existentes)

| Escalón | Qué | Precio | Por qué subir |
| --- | --- | --- | --- |
| Bueno | 1 síntoma (cobros, UCI-S2) | 99 € (39 + 60 al mejorar) | Entrada dentro del rango |
| Mejor | 2 síntomas | 198 € | Sin descuento (2 × 99): sirve de referencia |
| Óptimo | 3 síntomas | 249 € (99 + 150) | +51 € sobre el «mejor» da un síntoma más; 83 € cada uno |

El valor sigue siendo unos 250 €; solo cambia lo que se paga al entrar. Sin «antes costaba».

## 4. Qué ensayar primero

Dos precios dentro del rango, mismo paquete y garantía:
- **A:** 39 € ahora + 60 € cuando mejore (total 99 €).
- **B:** 99 € en un pago.

Cómo: en las 10 conversaciones del 8 de diciembre, A a la mitad y B a la otra, con enlace de Stripe. Se cuentan pagos, no «me interesa». Fijar antes la regla: A funciona si pagan al menos 2 de 10; si B iguala, mejor B (menos gestión). Con 0 de 10 en ambos, el freno es la confianza, no el precio.

No ensayar aún 198 ni 249 €. Antes, Maite fija por escrito qué es «mejora» en cada síntoma.

## 5. Cuándo sube de verdad el «precio inicial»

Hipótesis, con fecha anunciada: cuando haya 2 o 3 casos reales publicados con permiso y 3 compras de desconocidos al precio inicial. Después, subir dentro del rango (menos de 131 € por síntoma) y comprobar con compradores reales. Ir hacia 250 € por síntoma solo si pagan sin dudar; hoy ningún dato lo sostiene.

## 6. Objeciones de precio del panel (literales)

1. «99 € por un solo síntoma es mucho para mí, que apenas saco para vivir, y encima sin devolución.» (P008)
2. «Poder probar un síntoma por 30-40 € con devolución si no me mejora.»
3. «Me dejasen probar un primer paso de pago pequeño y viera algo concreto en mi cuenta en una semana.»

Respuesta: primer paso de 39 € y número propio desde el primer día. Sin devolución; se sigue sin coste hasta que mejore.
