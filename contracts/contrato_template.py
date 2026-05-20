"""
contrato_template.py — MAS@FRAME® v2 (10/10 clínico-premium)
Genera el HTML del Contrato Maestro Universal a partir de los datos del cliente.
Uso: html = generar_contrato_html(datos)
"""

from datetime import date

# ─── Planes ───────────────────────────────────────────────────────────────────
PLANES = {
    "PRE": {
        "nombre":        "Programa de Rescate Empresarial (PRE)",
        "ciclos":        "Protocolo C0–C6 completo sin ciclos clínicos digitales adicionales",
        "sintomas":      "Hasta 3 síntomas",
        "consultor":     "Asignación de CC en fase de diagnóstico",
        "duracion_meses": 3,
        "tiene_garantia": False,
    },
    "PAE": {
        "nombre":        "Programa de Activación Empresarial (PAE)",
        "ciclos":        "2 ciclos clínicos digitales con CC activo",
        "sintomas":      "De 4 a 6 síntomas",
        "consultor":     "CC activo en 2 ciclos",
        "duracion_meses": 6,
        "tiene_garantia": False,
    },
    "PIE": {
        "nombre":        "Programa de Intervención Empresarial (PIE)",
        "ciclos":        "3 ciclos clínicos digitales con CC presente en cada ciclo",
        "sintomas":      "De 7 a 10 síntomas",
        "consultor":     "CC presente en todos los ciclos",
        "duracion_meses": 12,
        "tiene_garantia": True,
    },
}

# ─── Cláusulas ────────────────────────────────────────────────────────────────
CLAUSULAS = [
    (
        "1. IDENTIFICACIÓN DE LAS PARTES",
        """<p>De una parte, <strong>MASESORA CONSULTING SL</strong>, titular del sistema clínico
        MAS@FRAME®, con NIF <strong>74860612M</strong>, con domicilio en Av. Gabriel Miró 27, 1 —
        Polop, Alicante (España), representada por <strong>María Teresa Cabezuelos Morcillo</strong>
        en calidad de Fundadora y Directora Clínica (en adelante, <em>La Clínica</em>).</p>
        <p>De otra parte, la empresa identificada en el encabezado de este contrato
        (en adelante, <em>El Cliente</em>), representada por la persona físia que suscribe
        el presente contrato con capacidad legal suficiente para obligar a su empresa.</p>"""
    ),
    (
        "2. OBJETO DEL CONTRATO Y NATURALEZA CLÍNICA",
        """<p>El presente contrato tiene por objeto la prestación de servicios de intervención
        clínica empresarial bajo el protocolo MAS@FRAME®, consistente en el diagnóstico,
        tratamiento estructurado y certificación del alta de los síntomas empresariales
        identificados en el Escáner ESE realizado por El Cliente.</p>
        <p><strong>MAS@FRAME® no es una consultoría convencional.</strong> Es un protocolo clínico
        empresarial basado en evidencia, compuesto por 7 capas secuenciales (C0–C6), con
        decisiones vinculantes, KPIs comprometidos, evidencias documentadas en cada capa
        y alta certificada por resultado real —no por tiempo transcurrido ni por formularios
        completados.</p>
        <p>Cada intervención genera un <strong>Expediente Clínico Empresarial (ECE)</strong>
        con evidencias, métricas, decisiones y verificaciones firmadas digitalmente por
        ambas partes. Este expediente es el único documento válido para la emisión del
        Certificado de Alta.</p>"""
    ),
    (
        "3. ALCANCE DE LA INTERVENCIÓN",
        """<p>El alcance queda definido exclusivamente por los síntomas contratados y el plan
        elegido, tal y como figuran en el encabezado del presente contrato.</p>
        <p><strong>Anexo I — KPIs Maestros:</strong> Este contrato incluye un Anexo I vinculante
        que documenta, para cada síntoma, el KPI de partida (valor C0), el criterio objetivo
        de alta y la fórmula de medición. El Anexo I <strong>se cumplimenta al inicio del protocolo
        de tratamiento</strong>, una vez completada la Capa C0 por el ACI y validada por el CC.
        Desde ese momento queda firmado digitalmente por ambas partes y es inamovible
        durante la vigencia del contrato.</p>
        <p>Cualquier ampliación del alcance —nuevos síntomas, planes adicionales o
        extensiones— requerirá un addendum firmado por ambas partes y el pago del importe
        correspondiente según la política de precios vigente en ese momento.</p>
        <p>El protocolo se aplica de forma secuencial e íntegra. No es posible omitir,
        reordenar ni abreviar las capas C0–C6 sin invalidar la trazabilidad clínica
        y la elegibilidad a garantía.</p>"""
    ),
    (
        "4. OBLIGACIONES DE EL CLIENTE",
        """<p>El Cliente asume expresamente las siguientes obligaciones, cuyo incumplimiento
        puede invalidar la trazabilidad clínica y eximir a La Clínica de garantía:</p>
        <ul>
        <li>Completar cada capa del protocolo C0–C6 en los plazos establecidos por el CC.</li>
        <li>Aportar datos <strong>reales, completos y verificables</strong> en cada capa. La aportación
            de datos falsos o incompletos invalida el expediente clínico.</li>
        <li>Ejecutar las acciones comprometidas en <strong>C2 (Decisión comprometida)</strong> sin
            modificaciones unilaterales no validadas por el CC.</li>
        <li>Actualizar los KPIs de seguimiento en C5 y C6 con información fidedigna y en los
            plazos acordados.</li>
        <li>Mantener absoluta confidencialidad sobre el contenido del protocolo, las
            herramientas, las matrices de decisión y los materiales propietarios de La Clínica.</li>
        <li>Informar al CC de cualquier cambio estratégico, organizativo o de mercado que
            pueda afectar a los KPIs comprometidos.</li>
        <li>Abonar los honorarios en los plazos y formas pactadas.</li>
        <li>No reproducir, adaptar, derivar, entrenar sistemas de IA ni utilizar el protocolo
            fuera del marco del presente contrato.</li>
        </ul>"""
    ),
    (
        "5. OBLIGACIONES DE LA CLÍNICA",
        """<ul>
        <li>Asignar un <strong>Consultor Clínico (CC)</strong> según el plan contratado, con la
            dedicación y presencia establecidas en el Anexo I.</li>
        <li>Aplicar el protocolo MAS@FRAME® con rigor metodológico y personalización
            al síntoma y contexto de El Cliente.</li>
        <li>Mantener la confidencialidad absoluta de todos los datos del cliente,
            salvo requerimiento legal expreso.</li>
        <li>Ejecutar el <strong>Precision Check</strong> en la semana 6 de cada ciclo clínico:
            evaluación automática del sistema que mide la coherencia entre las 7 capas
            y los KPIs comprometidos, y emite el veredicto de continuidad o alerta clínica.</li>
        <li>Emitir el <strong>Certificado de Alta</strong> cuando el sistema verifique que el
            KPI Maestro ha alcanzado el criterio establecido en el Anexo I y el CC
            valide las evidencias.</li>
        <li>Proporcionar acceso continuo a la plataforma clínica durante toda la vigencia
            del contrato.</li>
        <li>Activar los mecanismos de garantía establecidos en la Cláusula 8 cuando
            procedan, sin dilación ni negociación.</li>
        </ul>"""
    ),
    (
        "6. PROTOCOLO CLÍNICO C0–C6 Y KPI MAESTRO",
        """<p>El protocolo MAS@FRAME® se estructura en 7 capas clínicas de aplicación
        secuencial e irreversible. No es posible certificar una capa sin haber completado
        y documentado la anterior:</p>
        <ul>
        <li><strong>C0 — Diagnóstico KPI:</strong> Medición objetiva del estado actual del síntoma.
            Se define y documenta el <em>KPI Maestro</em>, su fórmula, fuente de datos,
            frecuencia de medición y valor inicial.</li>
        <li><strong>C1 — Priorización:</strong> Identificación de causas raíz, área de impacto
            y nivel de criticidad del síntoma.</li>
        <li><strong>C2 — Decisión comprometida:</strong> El Cliente firma las acciones concretas
            a ejecutar. Esta capa genera las obligaciones vinculantes del tratamiento.</li>
        <li><strong>C3 — Comprensión del proceso:</strong> Mapeo detallado de la intervención,
            timeline, recursos y criterios de éxito intermedios.</li>
        <li><strong>C4 — Cambio estructural:</strong> Sprint kanban de 4 semanas con tareas,
            responsables y entregas verificables.</li>
        <li><strong>C5 — Ejecución:</strong> OKRs activos + Cobrómetro® de valor generado.
            Seguimiento semanal del KPI Maestro.</li>
        <li><strong>C6 — Seguimiento y Alta:</strong> Verificación final del KPI Maestro.
            Comparación con valor C0. Emisión del veredicto y, si procede, del
            Certificado de Alta.</li>
        </ul>
        <p><strong>El KPI Maestro</strong> es la métrica principal del síntoma tratado. Se declara
        en C0 por el ACI, se valida en C1, se compromete en C2 y se certifica en C6.
        Su valor de partida, fórmula, fuente de datos, frecuencia de medición y criterio
        de alta quedan registrados en el <strong>Anexo I</strong>, que se genera y firma digitalmente
        al completar C0, siendo vinculante e inamovible para ambas partes a partir de ese momento.</p>
        <p>El alta solo se emite cuando el KPI Maestro alcanza el criterio objetivo con
        veredicto <strong>EXCELENTE</strong> u <strong>ÓPTIMO</strong>. No se certifica por completar
        formularios, sino por <strong>resultados reales documentados y verificados por el sistema.</strong></p>"""
    ),
    (
        "7. PLANES DE INTERVENCIÓN",
        """<p>Los planes de intervención MAS@FRAME® y sus condiciones estructurales son:</p>
        <table style="width:100%;border-collapse:collapse;margin-top:12px;font-size:0.85rem;">
        <thead>
        <tr style="background:#0F1A35;color:#F9F7F2;">
          <th style="padding:8px 12px;text-align:left;">Plan</th>
          <th style="padding:8px 12px;text-align:left;">Síntomas</th>
          <th style="padding:8px 12px;text-align:left;">Ciclos clínicos</th>
          <th style="padding:8px 12px;text-align:left;">Duración</th>
          <th style="padding:8px 12px;text-align:left;">Garantía</th>
        </tr>
        </thead>
        <tbody>
        <tr style="border-bottom:1px solid #e8e8e8;">
          <td style="padding:8px 12px;font-weight:700;">PRE</td>
          <td style="padding:8px 12px;">Hasta 3</td>
          <td style="padding:8px 12px;">C0–C6 completo</td>
          <td style="padding:8px 12px;">3 meses</td>
          <td style="padding:8px 12px;">No</td>
        </tr>
        <tr style="border-bottom:1px solid #e8e8e8;background:#fafafa;">
          <td style="padding:8px 12px;font-weight:700;">PAE</td>
          <td style="padding:8px 12px;">4 a 6</td>
          <td style="padding:8px 12px;">2 ciclos</td>
          <td style="padding:8px 12px;">6 meses</td>
          <td style="padding:8px 12px;">No</td>
        </tr>
        <tr>
          <td style="padding:8px 12px;font-weight:700;color:#B89D52;">PIE</td>
          <td style="padding:8px 12px;">7 a 10</td>
          <td style="padding:8px 12px;">3 ciclos</td>
          <td style="padding:8px 12px;">12 meses</td>
          <td style="padding:8px 12px;color:#B89D52;font-weight:700;">Total ✓</td>
        </tr>
        </tbody>
        </table>"""
    ),
    (
        "8. GARANTÍAS MAS@FRAME® — LO QUE EL SISTEMA CERTIFICA",
        """<p>Las garantías de MAS@FRAME® no son promesas comerciales. Son compromisos
        contractuales vinculantes, verificados automáticamente por el sistema y activables
        sin negociación. Se articulan en cinco principios:</p>

        <p><strong>Garantía 01 — El alta se gana con datos, no con tiempo.</strong><br/>
        Al contratar un síntoma se definen en contrato (Anexo I) los KPIs de partida (C0)
        y el criterio de alta (C6). Al cierre, el sistema compara KPIs iniciales y finales,
        revisa las evidencias del ACI y emite el veredicto. Si los criterios se cumplen,
        el CC firma el alta. Sin KPI objetivo documentado no existe alta clínica.</p>

        <p><strong>Garantía 02 — Precio fijo por tratamiento.</strong><br/>
        El Cliente conoce exactamente lo que paga antes de empezar. Sin horas facturables,
        sin extensiones de coste no pactadas, sin informes que nadie implementa. El importe
        queda fijado en el Anexo I y es inamovible durante la vigencia del contrato.</p>

        <p><strong>Garantía 03 — No invadimos la intimidad del negocio.</strong><br/>
        El ACI ejecuta el protocolo desde dentro de la empresa del Cliente. El CC supervisa,
        valida y firma el alta desde la plataforma. Sin consultores externos que pasen
        semanas en las instalaciones del Cliente. Sin acceso a información no estrictamente
        necesaria para el tratamiento del síntoma contratado.</p>

        <p><strong>Garantía 04 — El mismo protocolo, sin excepciones.</strong><br/>
        No hay interpretaciones subjetivas, ni atajos, ni adaptaciones no documentadas.
        Las 7 capas siempre en orden, siempre con entradas y salidas concretas. Lo que
        no se mide en C0 no puede certificarse en C6. La trazabilidad es total o el
        expediente queda invalidado.</p>

        <p><strong>Garantía 05 — Si el protocolo no funciona, no asumes el coste</strong>
        <span style="color:#B89D52;font-weight:600;">(exclusiva Plan PIE).</span><br/>
        En la semana 6 el <strong>Precision Check</strong> —el motor automático que evalúa la
        coherencia entre las 7 capas y los KPIs— emite el veredicto. Si el ACI ha cumplido
        con las evidencias y los objetivos no se han alcanzado, La Clínica amplía el
        tratamiento hasta <strong>3 meses sin coste adicional</strong>. Si tras ese periodo adicional
        el KPI Maestro sigue sin cumplir el criterio de alta, La Clínica <strong>devuelve el
        importe íntegro</strong>. Sin negociación. Sin interpretaciones. Sin condiciones adicionales.</p>

        <p style="background:#F8F6F0;border-left:3px solid #B89D52;padding:12px 16px;border-radius:0 6px 6px 0;margin-top:16px;font-size:0.85rem;">
        <strong>Condiciones de elegibilidad a garantía (Garantía 05):</strong> La garantía
        queda condicionada al cumplimiento íntegro de las obligaciones de El Cliente
        establecidas en la Cláusula 4 y a la ausencia de desviaciones del protocolo
        no autorizadas por el CC. Cualquier cambio estratégico, de equipo o de datos
        no comunicado al CC invalida la elegibilidad. El tope de garantía se fija
        por síntoma en el Anexo I.</p>"""
    ),
    (
        "9. DURACIÓN Y VIGENCIA",
        """<p>El presente contrato entra en vigor en la fecha de su firma digital y tiene
        una duración vinculada al plan contratado según lo establecido en el Anexo I.</p>
        <p>La finalización del contrato <strong>no implica la pérdida</strong> de acceso a los
        Certificados de Alta emitidos durante el período de vigencia. El Expediente
        Clínico Empresarial queda disponible en la plataforma de forma permanente.</p>
        <p>Los plazos de cada capa C0–C6 quedan fijados por el CC al inicio del
        tratamiento y pueden modificarse de mutuo acuerdo sin que ello altere el
        importe ni las condiciones de garantía, salvo que la modificación suponga
        una desviación del protocolo.</p>
        <p>La finalización anticipada del contrato no cancela los Certificados de Alta
        ya emitidos ni borra el Expediente Clínico Empresarial generado.</p>"""
    ),
    (
        "10. HONORARIOS Y FORMA DE PAGO",
        """<p>Los honorarios corresponden al importe del plan contratado, detallado en el
        <strong>Anexo I</strong> del presente contrato. El importe incluye la base imponible
        más el IVA aplicable (21%).</p>
        <p>El pago se realiza al inicio del tratamiento mediante los métodos habilitados
        en la plataforma (tarjeta bancaria, Stripe, transferencia bancaria). La confirmación
        del pago activa automáticamente el expediente clínico y el acceso a la plataforma.</p>
        <p>El importe pagado <strong>no es reembolsable</strong> salvo en los supuestos previstos
        en la Garantía 05 (Plan PIE) o por causas de resolución imputables exclusivamente
        a La Clínica.</p>"""
    ),
    (
        "11. CONFIDENCIALIDAD",
        """<p>Ambas partes se comprometen a mantener la más estricta confidencialidad sobre
        toda la información intercambiada en el marco del presente contrato, con carácter
        indefinido tras la finalización del mismo.</p>
        <p>La obligación de confidencialidad de El Cliente incluye expresamente: el
        protocolo C0–C6, las matrices de decisión, los OKRs clínicos, el Cobrómetro®,
        las herramientas de diagnóstico ESE, las plantillas de evidencia, los KPIs maestros
        acordados y cualquier otro material propietario de La Clínica.</p>
        <p>La Clínica no divulgará datos del cliente, del expediente clínico ni de los
        resultados del tratamiento a terceros, salvo requerimiento legal o autorización
        expresa del Cliente para uso como caso de estudio (siempre anonimizado).</p>"""
    ),
    (
        "12. PROPIEDAD INTELECTUAL Y PROTECCIÓN DEL SISTEMA",
        """<p>El Cliente reconoce y acepta que <strong>MAS@FRAME®</strong> es un sistema clínico
        propietario compuesto por, entre otros elementos: la arquitectura C0–C6, las
        nomenclaturas clínicas, los algoritmos de priorización ESE, las matrices de
        decisión, el Cobrómetro®, los OKRs clínicos empresariales, las herramientas
        de diagnóstico, las plantillas de evidencia, el sistema de certificación de
        altas y el Precision Check. Todos estos elementos constituyen propiedad
        intelectual de <strong>MASESORA CONSULTING SL</strong> y están protegidos por la
        legislación vigente de propiedad intelectual e industrial.</p>
        <p>Todo el contenido generado durante el tratamiento —incluyendo el Expediente
        Clínico Empresarial, las evidencias, los KPIs documentados y los certificados
        de alta— forma parte del expediente clínico del cliente y queda protegido bajo
        las mismas condiciones de confidencialidad.</p>
        <p>El Cliente <strong>no podrá</strong> en ningún caso: reproducir, adaptar, derivar,
        publicar, licenciar, sublicenciar, entrenar sistemas de inteligencia artificial,
        crear metodologías derivadas ni utilizar el protocolo o sus componentes fuera
        del marco estricto del presente contrato y de su propia organización. El
        incumplimiento de esta cláusula generará responsabilidad civil y penal en
        los términos previstos por la legislación española.</p>"""
    ),
    (
        "13. MARCO DE RESPONSABILIDAD CLÍNICA",
        """<p><strong>La Clínica</strong> será responsable de la correcta aplicación del protocolo
        MAS@FRAME® según la lex artis de la intervención clínica empresarial, de la
        asignación del CC competente y de la ejecución del Precision Check en los
        plazos establecidos.</p>
        <p><strong>El Cliente</strong> será responsable de: la veracidad y completitud de los datos
        aportados en cada capa; la ejecución íntegra de las acciones comprometidas en C2;
        la actualización puntual de los KPIs; y cualquier decisión empresarial tomada
        fuera del marco clínico acordado.</p>
        <p>Cualquier <strong>desviación del protocolo</strong> no autorizada expresamente por el CC —
        cambio de datos, omisión de capas, modificación de KPIs sin validación,
        incorporación de variables externas no declaradas— invalida la trazabilidad
        clínica, exime a La Clínica de toda responsabilidad sobre los resultados
        y cancela la elegibilidad a cualquier garantía.</p>
        <p>La responsabilidad máxima de La Clínica, en casos distintos a la Garantía 05,
        queda limitada al importe abonado por El Cliente en el marco del presente
        contrato, salvo en los supuestos de dolo o negligencia grave acreditada.</p>"""
    ),
    (
        "14. CAUSAS DE RESOLUCIÓN",
        """<p>El presente contrato podrá resolverse por:</p>
        <ul>
        <li>Mutuo acuerdo documentado entre las partes.</li>
        <li>Incumplimiento grave y reiterado de las obligaciones de cualquiera de las partes,
            previo requerimiento fehaciente con plazo de subsanación de 15 días.</li>
        <li>Imposibilidad sobrevenida y acreditada de prestación del servicio.</li>
        <li>Solicitud del Cliente con preaviso de 15 días naturales (sin reembolso del
            importe ya abonado, salvo Garantía 05 aplicable o resolución imputable a La Clínica).</li>
        <li>Incumplimiento de la cláusula de confidencialidad o propiedad intelectual
            por parte del Cliente, con efectos inmediatos y sin perjuicio de las
            acciones legales que procedan.</li>
        </ul>"""
    ),
    (
        "15. JURISDICCIÓN Y LEY APLICABLE",
        """<p>El presente contrato se rige íntegramente por la legislación española.
        Para la resolución de cualquier controversia derivada de su interpretación,
        ejecución o resolución, las partes se someten, con renuncia expresa a cualquier
        otro fuero que pudiera corresponderles, a los Juzgados y Tribunales de
        <strong>Alicante (España)</strong>.</p>"""
    ),
    (
        "16. CÓDIGO DEONTOLÓGICO MAS@FRAME®",
        """<p>El Consultor Clínico (CC) y el Agente Clínico Interno (ACI) quedan sujetos
        a los siguientes compromisos éticos, que forman parte inseparable del presente contrato:</p>
        <ul>
        <li>Aplicar el protocolo MAS@FRAME® con rigor, neutralidad y sin conflicto de intereses.</li>
        <li>No emitir el Certificado de Alta cuando los datos no lo justifiquen objetivamente,
            aunque exista presión por parte del Cliente.</li>
        <li>No aceptar retribuciones, regalos ni compensaciones del Cliente fuera del marco
            contractual pactado con La Clínica.</li>
        <li>Mantener la confidencialidad del expediente clínico con carácter indefinido,
            incluso tras la finalización del contrato.</li>
        <li>Comunicar al Cliente cualquier conflicto de interés que pudiera afectar
            a la objetividad del tratamiento.</li>
        <li>No recomendar acciones fuera del protocolo ni asumir compromisos no cubiertos
            por el presente contrato.</li>
        <li>Actuar en todo momento en beneficio de la salud empresarial del Cliente,
            con independencia de los resultados económicos para La Clínica.</li>
        </ul>
        <p>El incumplimiento de estos compromisos por parte del CC o del ACI da derecho
        al Cliente a comunicarlo a La Clínica, quien adoptará las medidas disciplinarias
        correspondientes sin perjuicio de las responsabilidades que pudieran derivarse.</p>"""
    ),
    (
        "17. PROTECCIÓN DE DATOS PERSONALES (RGPD)",
        """<p>De conformidad con el Reglamento (UE) 2016/679 (RGPD) y la Ley Orgánica
        3/2018 (LOPDGDD), La Clínica informa al Cliente de lo siguiente:</p>
        <ul>
        <li><strong>Responsable del tratamiento:</strong> MASESORA CONSULTING SL,
            NIF 74860612M, admin@masesora.com.</li>
        <li><strong>Finalidad:</strong> Gestión de la relación contractual, prestación del
            servicio clínico, emisión de facturas y certificados, y comunicaciones
            relacionadas con el expediente.</li>
        <li><strong>Base jurídica:</strong> Ejecución del contrato (art. 6.1.b RGPD) e
            interés legítimo en la correcta prestación del servicio.</li>
        <li><strong>Destinatarios:</strong> Los datos no se cederán a terceros salvo
            obligación legal. El acceso del CC y del ACI queda limitado estrictamente
            a los datos necesarios para la ejecución del protocolo.</li>
        <li><strong>Conservación:</strong> Los datos se conservarán durante la vigencia
            del contrato y por el período legal obligatorio (mínimo 5 años para
            documentación fiscal).</li>
        <li><strong>Derechos:</strong> El representante del Cliente puede ejercer los derechos
            de acceso, rectificación, supresión, limitación, portabilidad y oposición
            dirigiéndose a admin@masesora.com. Tiene derecho a reclamar ante la AEPD.</li>
        </ul>
        <p>La firma del presente contrato implica el consentimiento expreso al tratamiento
        de los datos personales del representante del Cliente en los términos descritos.</p>"""
    ),
    (
        "18. ACEPTACIÓN ÍNTEGRA — FIRMA DIGITAL",
        """<p>La firma digital del presente contrato constituye la manifestación expresa,
        libre e informada de la aceptación íntegra de todas las cláusulas aquí contenidas,
        incluyendo las condiciones generales del servicio clínico, el código deontológico
        MAS@FRAME®, el tratamiento de datos conforme al RGPD, y el detalle del plan
        contratado con sus KPIs maestros y riesgos asumidos.</p>
        <p>El Cliente declara haber leído, comprendido y aceptado la totalidad del contrato
        antes de proceder a su firma. No existirán condiciones adicionales, compromisos
        verbales ni documentos adjuntos que amplíen o modifiquen lo aquí establecido,
        salvo addendum escrito y firmado por ambas partes.</p>
        <p style="font-weight:600;color:#0F1A35;margin-top:10px;">
        Con la firma de este contrato queda formalizada la relación clínica entre
        El Cliente y La Clínica, y activado el Expediente Clínico Empresarial
        en la plataforma MAS@FRAME®.</p>"""
    ),
]


# ─── Generador HTML ───────────────────────────────────────────────────────────
def generar_contrato_html(datos: dict) -> str:
    """
    Genera el HTML completo del Contrato Maestro Universal MAS@FRAME®.

    datos = {
        "codigo":        str,   # Código del expediente
        "razon_social":  str,
        "cif":           str,
        "representante": str,
        "cargo":         str,
        "email":         str,
        "telefono":      str,
        "direccion":     str,
        "ciudad":        str,
        "codigo_postal": str,
        "plan":          str,   # "PRE" | "PAE" | "PIE"
        "sintomas":      list[str],
        "importe":       float,
        "fecha":         str,   # "YYYY-MM-DD"
    }
    """
    plan_key  = datos.get("plan", "PRE").upper()
    plan_info = PLANES.get(plan_key, PLANES["PRE"])
    hoy       = datos.get("fecha", date.today().isoformat())
    year      = hoy[:4]
    num_contrato = f"MASF-{year}-{datos.get('codigo','')}"
    importe   = float(datos.get("importe", 0))
    iva       = round(importe * 0.21, 2)
    total_iva = round(importe + iva, 2)

    sintomas_list  = datos.get("sintomas", [])
    sintomas_html  = "".join(
        f'<span style="display:inline-block;background:rgba(15,26,53,0.06);'
        f'color:#0F1A35;font-family:monospace;font-size:0.78rem;'
        f'padding:3px 10px;border-radius:999px;margin:3px;">{s}</span>'
        for s in sintomas_list
    )

    # Filas KPI por síntoma en Anexo I
    kpi_rows_html = ""
    for s in sintomas_list:
        kpi_rows_html += f"""
        <tr>
          <td style="padding:8px 10px;border-bottom:1px solid #eee;font-size:0.82rem;
                     font-weight:500;color:#0F1A35;">{s}</td>
          <td style="padding:8px 10px;border-bottom:1px solid #eee;"></td>
          <td style="padding:8px 10px;border-bottom:1px solid #eee;text-align:center;"></td>
          <td style="padding:8px 10px;border-bottom:1px solid #eee;text-align:center;"></td>
          <td style="padding:8px 10px;border-bottom:1px solid #eee;text-align:center;"></td>
          {'<td style="padding:8px 10px;border-bottom:1px solid #eee;text-align:center;"></td>' if plan_info["tiene_garantia"] else ''}
        </tr>"""

    garantia_th = '<th style="padding:8px 10px;text-align:center;">Tope garantía</th>' if plan_info["tiene_garantia"] else ""

    clausulas_html = ""
    for titulo, cuerpo in CLAUSULAS:
        clausulas_html += f"""
        <div class="clausula">
          <h3 class="clausula-titulo">{titulo}</h3>
          <div class="clausula-cuerpo">{cuerpo}</div>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Contrato MAS@FRAME® · {num_contrato}</title>
<link rel="icon" href="https://www.masesora.com/assets/favicon.svg"/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet"/>
<style>
  *{{box-sizing:border-box;margin:0;padding:0;}}
  html{{font-size:16px;}}
  body{{
    background:#F4F1EB;
    font-family:'DM Sans',sans-serif;
    color:#1A1A1A;
    -webkit-print-color-adjust:exact;
    print-color-adjust:exact;
  }}

  /* ── PORTADA ── */
  .portada{{
    background:#0F1A35;
    min-height:100vh;
    display:flex;flex-direction:column;
    align-items:center;justify-content:center;
    padding:80px 60px;
    position:relative;
    page-break-after:always;
  }}
  .portada::before{{
    content:'';position:absolute;inset:0;
    background-image:linear-gradient(rgba(184,157,82,.06) 1px,transparent 1px),
      linear-gradient(90deg,rgba(184,157,82,.06) 1px,transparent 1px);
    background-size:44px 44px;
  }}
  .portada-top-line{{
    position:absolute;top:0;left:0;right:0;height:3px;
    background:linear-gradient(90deg,#C8A84B,#E8C96A,#B89D52);
  }}
  .portada-logo{{
    font-family:'Cormorant Garamond',serif;
    font-size:2.6rem;font-weight:700;
    color:#F9F7F2;letter-spacing:6px;
    margin-bottom:6px;position:relative;z-index:1;
  }}
  .portada-subtitulo{{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.68rem;color:#B89D52;
    letter-spacing:4px;text-transform:uppercase;
    margin-bottom:80px;position:relative;z-index:1;
  }}
  .portada-badge{{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.62rem;color:#B89D52;
    letter-spacing:3px;text-transform:uppercase;
    margin-bottom:16px;position:relative;z-index:1;
  }}
  .portada-titulo{{
    font-family:'Cormorant Garamond',serif;
    font-size:3rem;font-weight:700;
    color:#F9F7F2;text-align:center;
    line-height:1.15;margin-bottom:12px;
    position:relative;z-index:1;
  }}
  .portada-num{{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.85rem;color:rgba(249,247,242,0.45);
    letter-spacing:2px;margin-bottom:60px;
    position:relative;z-index:1;
  }}
  .portada-data{{
    display:flex;gap:48px;flex-wrap:wrap;justify-content:center;
    position:relative;z-index:1;
  }}
  .portada-dato{{text-align:center;}}
  .portada-dato-label{{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.6rem;color:rgba(184,157,82,0.65);
    letter-spacing:2px;text-transform:uppercase;margin-bottom:6px;
  }}
  .portada-dato-val{{
    font-family:'DM Sans',sans-serif;
    font-size:0.95rem;font-weight:600;
    color:rgba(249,247,242,0.85);
  }}
  .portada-divider{{
    width:80px;height:1px;
    background:linear-gradient(90deg,transparent,#B89D52,transparent);
    margin:40px auto;position:relative;z-index:1;
  }}

  /* ── CUERPO ── */
  .cuerpo{{max-width:820px;margin:0 auto;padding:60px 48px 80px;}}

  /* ── PARTES ── */
  .partes-box{{
    background:#fff;border:1px solid #E8E8E8;
    border-left:4px solid #B89D52;
    border-radius:12px;padding:28px 32px;margin-bottom:40px;
  }}
  .partes-grid{{display:flex;gap:40px;flex-wrap:wrap;}}
  .parte-col{{flex:1;min-width:200px;}}
  .parte-label{{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.6rem;color:#B89D52;
    letter-spacing:3px;text-transform:uppercase;margin-bottom:10px;
  }}
  .parte-nombre{{
    font-family:'Cormorant Garamond',serif;
    font-size:1.25rem;font-weight:700;color:#0F1A35;margin-bottom:4px;
  }}
  .parte-dato{{font-size:0.82rem;color:#555;line-height:1.7;}}

  /* ── ANEXO I ── */
  .anexo-box{{
    background:#fff;border:1px solid #E8E8E8;
    border-radius:12px;padding:28px 32px;margin-bottom:40px;
  }}
  .anexo-titulo{{
    font-family:'Cormorant Garamond',serif;
    font-size:1.3rem;font-weight:700;color:#0F1A35;
    margin-bottom:20px;padding-bottom:12px;
    border-bottom:1px solid #E8E8E8;
  }}
  .anexo-grid{{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:20px;}}
  .anexo-item{{
    flex:1;min-width:150px;
    background:#F8F6F0;border-radius:8px;padding:14px 16px;
  }}
  .anexo-item-label{{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.58rem;color:#999;
    letter-spacing:2px;text-transform:uppercase;margin-bottom:5px;
  }}
  .anexo-item-val{{font-size:0.92rem;font-weight:600;color:#0F1A35;}}
  .sintomas-label{{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.6rem;color:#999;
    letter-spacing:2px;text-transform:uppercase;margin-bottom:8px;
  }}
  .kpi-table{{
    width:100%;border-collapse:collapse;font-size:0.82rem;margin-top:16px;
  }}
  .kpi-table thead tr{{background:#0F1A35;color:#F9F7F2;}}
  .kpi-table thead th{{
    padding:8px 10px;text-align:left;
    font-family:'IBM Plex Mono',monospace;
    font-size:0.58rem;letter-spacing:1.5px;text-transform:uppercase;
    font-weight:400;
  }}
  .fill-line{{
    height:32px;border:1px dashed #CBD5E1;border-radius:4px;margin-top:6px;
  }}
  .riesgos-box{{
    background:#FFF8F0;border:1px solid #F0D9B5;
    border-left:3px solid #E8A020;
    border-radius:0 8px 8px 0;
    padding:16px 20px;margin-top:20px;font-size:0.83rem;
  }}

  /* ── GARANTÍAS HIGHLIGHT ── */
  .garantia-highlight{{
    background:linear-gradient(135deg,#0F1A35 0%,#1a2d5a 100%);
    border-radius:12px;padding:28px 32px;margin-bottom:40px;
    border:1px solid rgba(184,157,82,0.3);
  }}
  .garantia-highlight-titulo{{
    font-family:'Cormorant Garamond',serif;
    font-size:1.25rem;font-weight:700;color:#E8C96A;
    letter-spacing:1px;margin-bottom:20px;
  }}
  .garantia-item{{
    display:flex;gap:16px;margin-bottom:16px;align-items:flex-start;
  }}
  .garantia-num{{
    font-family:'IBM Plex Mono',monospace;
    font-size:1.2rem;font-weight:700;color:#B89D52;
    min-width:36px;
  }}
  .garantia-text{{font-size:0.85rem;color:rgba(249,247,242,0.8);line-height:1.6;}}
  .garantia-text strong{{color:#F9F7F2;}}

  /* ── CLÁUSULAS ── */
  .clausulas-titulo{{
    font-family:'Cormorant Garamond',serif;
    font-size:1.6rem;font-weight:700;color:#0F1A35;
    margin-bottom:32px;padding-bottom:14px;
    border-bottom:2px solid #0F1A35;
  }}
  .clausula{{margin-bottom:32px;}}
  .clausula-titulo{{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.72rem;font-weight:500;
    color:#B89D52;letter-spacing:2px;
    text-transform:uppercase;margin-bottom:10px;
  }}
  .clausula-cuerpo{{font-size:0.9rem;line-height:1.8;color:#333;}}
  .clausula-cuerpo p{{margin-bottom:10px;}}
  .clausula-cuerpo ul{{padding-left:20px;}}
  .clausula-cuerpo li{{margin-bottom:6px;}}
  .clausula-cuerpo table{{font-size:0.82rem;}}

  /* ── FIRMAS ── */
  .firmas-section{{
    margin-top:64px;padding-top:40px;
    border-top:1px solid #E8E8E8;
  }}
  .firmas-titulo{{
    font-family:'Cormorant Garamond',serif;
    font-size:1.3rem;font-weight:700;color:#0F1A35;
    margin-bottom:32px;text-align:center;
  }}
  .firmas-grid{{display:flex;gap:40px;flex-wrap:wrap;}}
  .firma-col{{
    flex:1;min-width:240px;
    background:#fff;border:1px solid #E8E8E8;
    border-radius:12px;padding:24px;text-align:center;
  }}
  .firma-label{{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.6rem;color:#999;
    letter-spacing:2px;text-transform:uppercase;margin-bottom:16px;
  }}
  .firma-nombre{{font-size:0.82rem;color:#0F1A35;font-weight:600;margin-bottom:2px;}}
  .firma-fecha{{
    font-family:'IBM Plex Mono',monospace;font-size:0.65rem;color:#999;
  }}

  /* ── FOOTER ── */
  .footer{{
    margin-top:48px;padding-top:24px;
    border-top:1px solid #E8E8E8;text-align:center;
  }}
  .footer-txt{{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.6rem;color:#BBB;letter-spacing:1.5px;
    text-transform:uppercase;line-height:2;
  }}

  /* ── PRINT ── */
  @media print{{
    body{{background:#fff;}}
    .portada{{min-height:auto;padding:60px;}}
    .no-print{{display:none!important;}}
    .clausula{{page-break-inside:avoid;}}
    .firmas-section{{page-break-inside:avoid;}}
    .garantia-highlight{{page-break-inside:avoid;}}
  }}
</style>
</head>
<body>

<!-- ══ PORTADA ══ -->
<div class="portada">
  <div class="portada-top-line"></div>
  <div class="portada-logo">MAS@FRAME®</div>
  <div class="portada-subtitulo">Sistema Clínico de Intervención Empresarial</div>
  <div class="portada-badge">Contrato de Prestación de Servicios Clínicos · Instrumento Jurídico</div>
  <div class="portada-titulo">Contrato Maestro<br/>Universal</div>
  <div class="portada-num">{num_contrato}</div>
  <div class="portada-divider"></div>
  <div class="portada-data">
    <div class="portada-dato">
      <div class="portada-dato-label">Empresa</div>
      <div class="portada-dato-val">{datos.get('razon_social','—')}</div>
    </div>
    <div class="portada-dato">
      <div class="portada-dato-label">Plan</div>
      <div class="portada-dato-val">{plan_key}</div>
    </div>
    <div class="portada-dato">
      <div class="portada-dato-label">Fecha</div>
      <div class="portada-dato-val">{hoy}</div>
    </div>
    <div class="portada-dato">
      <div class="portada-dato-label">Importe total</div>
      <div class="portada-dato-val">{total_iva:,.0f} € (IVA inc.)</div>
    </div>
  </div>
</div>

<!-- ══ CUERPO ══ -->
<div class="cuerpo">

  <!-- Partes -->
  <div class="partes-box">
    <div class="partes-grid">
      <div class="parte-col">
        <div class="parte-label">La Clínica</div>
        <div class="parte-nombre">MASESORA CONSULTING SL</div>
        <div class="parte-dato">
          María Teresa Cabezuelos Morcillo<br/>
          NIF 74860612M · Fundadora &amp; Directora Clínica<br/>
          Av. Gabriel Miró 27, 1 — Polop, Alicante<br/>
          admin@masesora.com · +34 609 987 436
        </div>
      </div>
      <div class="parte-col">
        <div class="parte-label">El Cliente</div>
        <div class="parte-nombre">{datos.get('razon_social','—')}</div>
        <div class="parte-dato">
          {datos.get('representante','—')} · {datos.get('cargo','')}<br/>
          CIF/NIF: {datos.get('cif','—')}<br/>
          {datos.get('direccion','—')}, {datos.get('ciudad','—')} {datos.get('codigo_postal','')}<br/>
          {datos.get('email','—')} · {datos.get('telefono','—')}
        </div>
      </div>
    </div>
  </div>

  <!-- Garantías highlight (previo a Anexo I para posicionamiento) -->
  <div class="garantia-highlight">
    <div class="garantia-highlight-titulo">Las 5 Garantías MAS@FRAME® — Lo que el sistema certifica</div>
    <div class="garantia-item">
      <div class="garantia-num">01</div>
      <div class="garantia-text"><strong>El alta se gana con datos, no con tiempo.</strong> Los KPIs de partida y el criterio de alta quedan definidos en el Anexo I. El sistema emite el veredicto al cierre de C6.</div>
    </div>
    <div class="garantia-item">
      <div class="garantia-num">02</div>
      <div class="garantia-text"><strong>Precio fijo por tratamiento.</strong> Sin horas facturables, sin sorpresas al final. El importe queda fijado en el Anexo I y es inamovible.</div>
    </div>
    <div class="garantia-item">
      <div class="garantia-num">03</div>
      <div class="garantia-text"><strong>No invadimos la intimidad del negocio.</strong> El ACI ejecuta desde dentro. El CC supervisa y firma el alta desde la plataforma. Sin acceso a lo que no necesitan ver.</div>
    </div>
    <div class="garantia-item">
      <div class="garantia-num">04</div>
      <div class="garantia-text"><strong>El mismo protocolo, sin excepciones.</strong> Las 7 capas siempre en orden, siempre con entradas y salidas concretas. Lo que no se mide en C0 no puede certificarse en C6.</div>
    </div>
    <div class="garantia-item">
      <div class="garantia-num">05</div>
      <div class="garantia-text">
        <strong>Si el protocolo no funciona, no asumes el coste.</strong>
        {"<span style='color:#E8C96A;'> Activa para Plan PIE.</span> Si el ACI cumple y el KPI Maestro no alcanza el criterio, La Clínica extiende 3 meses sin coste. Si sigue sin cumplirse, devuelve el importe íntegro. Sin negociación." if plan_info["tiene_garantia"] else "<span style='color:rgba(249,247,242,0.4);'> No aplica al plan contratado.</span>"}
      </div>
    </div>
  </div>

  <!-- Anexo I -->
  <div class="anexo-box">
    <div class="anexo-titulo">📎 Anexo I — Detalle del Plan Contratado</div>
    <div class="anexo-grid">
      <div class="anexo-item">
        <div class="anexo-item-label">Plan</div>
        <div class="anexo-item-val" style="color:#B89D52;">{plan_key} — {plan_info['nombre']}</div>
      </div>
      <div class="anexo-item">
        <div class="anexo-item-label">Duración</div>
        <div class="anexo-item-val">{plan_info['duracion_meses']} meses</div>
      </div>
      <div class="anexo-item">
        <div class="anexo-item-label">Ciclos clínicos</div>
        <div class="anexo-item-val">{plan_info['ciclos']}</div>
      </div>
      <div class="anexo-item">
        <div class="anexo-item-label">Consultor (CC)</div>
        <div class="anexo-item-val">{plan_info['consultor']}</div>
      </div>
    </div>
    <div class="anexo-grid">
      <div class="anexo-item">
        <div class="anexo-item-label">Base imponible</div>
        <div class="anexo-item-val">{importe:,.2f} €</div>
      </div>
      <div class="anexo-item">
        <div class="anexo-item-label">IVA (21%)</div>
        <div class="anexo-item-val">{iva:,.2f} €</div>
      </div>
      <div class="anexo-item">
        <div class="anexo-item-label">Total</div>
        <div class="anexo-item-val" style="color:#0F1A35;font-size:1.1rem;">{total_iva:,.2f} €</div>
      </div>
      <div class="anexo-item">
        <div class="anexo-item-label">Fecha de inicio</div>
        <div class="anexo-item-val">{hoy}</div>
      </div>
    </div>

    <!-- Síntomas y tabla KPI -->
    <div class="sintomas-label" style="margin-top:8px;">Síntomas contratados y KPIs Maestros</div>
    {f'<div style="margin-bottom:12px;">{sintomas_html}</div>' if sintomas_html else '<p style="color:#999;font-size:0.85rem;margin-bottom:12px;">Pendiente de asignación por CC</p>'}

    <table class="kpi-table">
      <thead>
        <tr>
          <th>Síntoma</th>
          <th>KPI Maestro y fórmula</th>
          <th>Valor C0 (inicial)</th>
          <th>Objetivo C2</th>
          <th>Criterio alta C6</th>
          {garantia_th}
        </tr>
      </thead>
      <tbody>
        {kpi_rows_html if kpi_rows_html else '<tr><td colspan="6" style="padding:12px;color:#999;font-size:0.82rem;text-align:center;">A completar por CC en C0</td></tr>'}
      </tbody>
    </table>

    <!-- Riesgos asumidos por el cliente -->
    <div class="riesgos-box">
      <div style="font-family:'IBM Plex Mono',monospace;font-size:0.6rem;letter-spacing:2px;
                  text-transform:uppercase;color:#E8A020;margin-bottom:8px;">
        Riesgos asumidos por El Cliente</div>
      <p style="color:#7A5A20;line-height:1.6;">
        El Cliente declara conocer y asumir expresamente que: (a) la falta de datos
        fidedignos en C0 invalida el criterio de alta; (b) el incumplimiento de las
        acciones comprometidas en C2 exime a La Clínica de la garantía; (c) cualquier
        decisión estratégica tomada fuera del marco del protocolo no está cubierta por
        la responsabilidad clínica de La Clínica; (d) los resultados dependen
        parcialmente de factores externos no controlables por el sistema.
      </p>
    </div>

    <div style="margin-top:20px;padding-top:16px;border-top:1px dashed #E8E8E8;">
      <div class="anexo-item-label">CC asignado al expediente (a completar por La Clínica)</div>
      <div class="fill-line"></div>
    </div>
  </div>

  <!-- Cláusulas -->
  <div class="clausulas-titulo">Condiciones Generales del Servicio Clínico</div>
  {clausulas_html}

  <!-- Firmas -->
  <div class="firmas-section">
    <div class="firmas-titulo">Firmas de las Partes</div>
    <p style="text-align:center;font-size:0.83rem;color:#666;margin-bottom:28px;">
      La firma digital de este documento implica la aceptación íntegra de las condiciones
      generales, el Anexo I y los Anexos II y III incorporados por referencia.
    </p>
    <div class="firmas-grid">
      <div class="firma-col">
        <div class="firma-label">La Clínica · MASESORA CONSULTING SL</div>
        <div style="height:80px;display:flex;align-items:center;justify-content:center;
                    border:1px solid #E8E8E8;border-radius:8px;margin-bottom:12px;
                    font-size:0.8rem;color:#BBB;font-style:italic;">
          Firma Maite Cabezuelos
        </div>
        <div class="firma-nombre">María Teresa Cabezuelos Morcillo</div>
        <div class="firma-fecha">NIF 74860612M · Directora Clínica · {hoy}</div>
      </div>
      <div class="firma-col">
        <div class="firma-label">El Cliente</div>
        <canvas id="firmaCliente" width="400" height="100"
          style="width:100%;height:100px;border:1px dashed #CBD5E1;border-radius:8px;
                 cursor:crosshair;display:block;margin-bottom:12px;touch-action:none;">
        </canvas>
        <div class="firma-nombre">{datos.get('representante','—')}</div>
        <div class="firma-fecha">{datos.get('razon_social','—')} · <span id="fechaFirma">Pendiente de firma</span></div>
        <div style="display:flex;gap:8px;justify-content:center;margin-top:12px;" class="no-print">
          <button onclick="limpiarFirma()" style="background:none;border:1px solid #CBD5E1;
            border-radius:6px;padding:5px 12px;font-size:0.75rem;cursor:pointer;color:#666;">
            Limpiar</button>
          <button onclick="guardarFirma()" style="background:#0F1A35;border:none;
            border-radius:6px;padding:5px 14px;font-size:0.75rem;cursor:pointer;
            color:#F9F7F2;font-weight:600;">✓ Firmar contrato</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <div class="footer">
    <div class="footer-txt">
      MASESORA CONSULTING SL · NIF 74860612M · Sistema Clínico MAS@FRAME® · www.masesora.com<br/>
      {num_contrato} · Generado el {hoy} · Documento confidencial — 18 cláusulas · Contrato completo autocontenido
    </div>
  </div>

</div>

<!-- Botón PDF -->
<div class="no-print" style="position:fixed;bottom:24px;right:24px;display:flex;gap:10px;z-index:999;">
  <button onclick="window.print()" style="
    background:linear-gradient(135deg,#B89D52,#E8C96A);color:#0F1A35;
    border:none;border-radius:999px;padding:12px 24px;
    font-family:'IBM Plex Mono',monospace;font-size:0.8rem;font-weight:700;
    letter-spacing:0.08em;cursor:pointer;
    box-shadow:0 4px 20px rgba(184,157,82,0.4);
  ">⬇ Descargar PDF</button>
</div>

<script>
const canvas = document.getElementById('firmaCliente');
const ctx    = canvas.getContext('2d');
let drawing  = false;
let hasFirma = false;

function pos(e) {{
  const r = canvas.getBoundingClientRect();
  return [(e.clientX-r.left)*(canvas.width/r.width),
          (e.clientY-r.top)*(canvas.height/r.height)];
}}

canvas.addEventListener('mousedown',  e => {{ drawing=true; ctx.beginPath(); ctx.moveTo(...pos(e)); }});
canvas.addEventListener('mousemove',  e => {{ if(!drawing) return; ctx.lineWidth=2; ctx.lineCap='round'; ctx.strokeStyle='#0F1A35'; ctx.lineTo(...pos(e)); ctx.stroke(); }});
canvas.addEventListener('mouseup',    ()=> {{ drawing=false; hasFirma=true; }});
canvas.addEventListener('mouseleave', ()=> {{ drawing=false; }});
canvas.addEventListener('touchstart', e => {{ e.preventDefault(); drawing=true; ctx.beginPath(); ctx.moveTo(...pos(e.touches[0])); }}, {{passive:false}});
canvas.addEventListener('touchmove',  e => {{ e.preventDefault(); if(!drawing) return; ctx.lineWidth=2; ctx.lineCap='round'; ctx.strokeStyle='#0F1A35'; ctx.lineTo(...pos(e.touches[0])); ctx.stroke(); }}, {{passive:false}});
canvas.addEventListener('touchend',   ()=> {{ drawing=false; hasFirma=true; }});

function limpiarFirma() {{
  ctx.clearRect(0,0,canvas.width,canvas.height);
  hasFirma=false;
  document.getElementById('fechaFirma').textContent='Pendiente de firma';
}}

function guardarFirma() {{
  if(!hasFirma) {{ alert('Por favor, dibuja tu firma antes de confirmar.'); return; }}
  const firmaBase64 = canvas.toDataURL('image/png');
  const fecha = new Date().toLocaleDateString('es-ES',{{day:'2-digit',month:'2-digit',year:'numeric'}});
  document.getElementById('fechaFirma').textContent = fecha;

  const params = new URLSearchParams(window.location.search);
  const codigo = params.get('codigo') || '';

  if (codigo) {{
    fetch('/contracts/firmar/' + codigo, {{
      method: 'POST',
      headers: {{'Content-Type':'application/json'}},
      body: JSON.stringify({{ firma_base64: firmaBase64, fecha_firma: fecha }})
    }})
    .then(r => r.json())
    .then(() => {{
      if (window.parent !== window) {{
        window.parent.postMessage({{ tipo:'contrato_firmado', codigo, fecha }}, '*');
      }}
    }})
    .catch(console.error);
  }}

  alert('✓ Contrato firmado correctamente. Puedes descargarlo en PDF con el botón inferior.');
}}
</script>
</body>
</html>"""
