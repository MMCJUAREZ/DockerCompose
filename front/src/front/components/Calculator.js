import React, { useState, useEffect } from "react";
import axios from "axios";

const API_URL = "http://localhost:8000/operaciones";

function Calculator() {
  const [valor1, setValor1] = useState("");
  const [valor2, setValor2] = useState("");
  const [resultado, setResultado] = useState(null);
  const [historial, setHistorial] = useState([]);

  useEffect(() => {
    obtenerHistorial();
  }, []);

  const obtenerHistorial = async () => {
    const res = await axios.get(`${API_URL}/historial`);
    setHistorial(res.data);
  };

  const operar = async (tipo) => {
    const endpoint = tipo === "suma" ? "sumar" : "multiplicar";
    const res = await axios.post(`${API_URL}/${endpoint}`, {
      valor1: parseFloat(valor1),
      valor2: parseFloat(valor2),
    });
    setResultado(res.data.resultado);
    obtenerHistorial();
  };

  return (
    <div>
      <input
        type="number"
        value={valor1}
        onChange={(e) => setValor1(e.target.value)}
        placeholder="Valor 1"
      />
      <input
        type="number"
        value={valor2}
        onChange={(e) => setValor2(e.target.value)}
        placeholder="Valor 2"
      />
      <button onClick={() => operar("suma")}>Sumar</button>
      <button onClick={() => operar("multiplicar")}>Multiplicar</button>
      {resultado !== null && <div>Resultado: {resultado}</div>}
      <h2>Historial</h2>
      <ul>
        {historial.map((op) => (
          <li key={op.id}>
            [{op.timestamp}] {op.tipo}: {op.valor1} y {op.valor2} = {op.resultado}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Calculator;