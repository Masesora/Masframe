const fs = require("fs");

function cleanField(value) {
  if (typeof value !== "string") return value;

  // Quitar comillas externas
  value = value.replace(/^"(.*)"$/, "$1");

  // Convertir \\n en saltos reales
  value = value.replace(/\\n/g, "\n");

  return value;
}

const data = JSON.parse(fs.readFileSync("symptoms.json", "utf8"));

const cleaned = data.map(item => {
  const newItem = { ...item };
  for (const key in newItem) {
    newItem[key] = cleanField(newItem[key]);
  }
  return newItem;
});

fs.writeFileSync("symptoms_clean.json", JSON.stringify(cleaned, null, 2));
console.log("JSON limpiado → symptoms_clean.json");