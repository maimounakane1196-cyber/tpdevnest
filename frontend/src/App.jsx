import { useEffect, useState } from 'react'

export default function App() {
  const [status, setStatus] = useState('...')

  // Au chargement, on demande au backend s'il est en vie
  useEffect(() => {
    fetch('http://localhost:8000/health')
      .then((res) => res.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus('backend injoignable'))
  }, [])

  return (
    <div>
      <h1>TP CI/CD</h1>
      <p>Statut du backend : {status}</p>
    </div>
  )
}