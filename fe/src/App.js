import "./App.css";
import {useState} from "react";
import axios from "axios";

function App() {
  const [input, setInput] = useState("0");
  const [oddNumber, setOddNumber] = useState("");
  const [primeNumber, setPrimeNumber] = useState("");
  const [triangleNumber, setTriangleNumber] = useState("");

  const onChange = (event) => {
    setInput(event);
  };


  const onPressTriangle = async () => {
    if (input && input > 0) {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/star-triangle/",
          {
            number: input,
          }
        );
        setTriangleNumber(response.data?.triangle);
      } catch (error) {
        alert(`Something went wrong ERR ${error}`);
      }
    } else {
      alert("Input cannot be empty and should be number");
    }
  };

  const onPressOddNumbers = async () => {
    if (input && input > 0) {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/odd-numbers/",
          {
            number: input,
          }
        );
        setOddNumber(response.data.odd_numbers);
      } catch (error) {
        alert(`Something went wrong ERR ${error}`);
      }
    } else {
      alert("Input cannot be empty and should be number");
    }
  };

  const onPressPrimeNumbers = async () => {
    if (input && input > 0) {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/prime-number/",
          {
            number: input,
          }
        );
        setPrimeNumber(response.data);
      } catch (error) {
        alert(`Something went wrong ERR ${error}`);
      }
    } else {
      alert("Input cannot be empty and should be number");
    }
  };



  return (
    <div className="App">
      <input
        placeholder="input angka"
        type="number"
        className="input-number"
        value={input}
        onChange={(e) => onChange(e.target.value)}
      />
      <div className="container-button">
        <button className="button" onClick={onPressTriangle}>
          Generate Segitiga
        </button>
        <button className="button" onClick={onPressOddNumbers}>
          Generate Bilangan Ganjil
        </button>
        <button className="button" onClick={onPressPrimeNumbers}>
          Generate Bilangan Prima
        </button>
      </div>

      <h2>Result</h2>
      <br />
      <p>
        <pre>
          <pre>
            {triangleNumber && triangleNumber}
          </pre>
        </pre>
      </p>
      <br />
      <p>{oddNumber && `Odd Number : ${oddNumber?.toString()}`}</p>
      <br />
      <p>
        {primeNumber &&
          ` ${primeNumber?.number} Is Prime : ${primeNumber?.is_prime}`}
      </p>
      <br />
    </div>
  );
}

export default App;
