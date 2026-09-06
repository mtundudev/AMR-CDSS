import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard.jsx";
import DashboardLayout from "./layouts/DashboardLayout.jsx";
import NewAnalysis from "./pages/NewAnalysis.jsx";
import AnalysisHistory from "./pages/AnalysisHistory.jsx";

export default function App() {
    return (
        <BrowserRouter>
            <DashboardLayout>
                <Routes>
                    <Route path="/" element={<Dashboard />} />
                    <Route path="/new-analysis" element={<NewAnalysis />} />
                    <Route path="/history" element={<AnalysisHistory />} />
                </Routes>
            </DashboardLayout>
        </BrowserRouter>
    );
}