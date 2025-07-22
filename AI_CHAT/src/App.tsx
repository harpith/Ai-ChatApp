// App.tsx
import { BrowserRouter, Routes, Route } from "react-router-dom"
import MainLayout from "./components/MainLayout"
import HomePage from "./Pages/HomePage"

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          <Route index element={<HomePage />} />
          </Route>
      
      </Routes>
    </BrowserRouter>
  )
}

export default App
