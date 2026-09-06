import Sidebar from "../components/sidebar.jsx";
import Header from "../components/Header.jsx";


export default function DashboardLayout ({children}){
    return(
        <>

        <div className={"min-h-screen bg-slate-50 text-slate-900"}>
            <Sidebar/>

            <div className={"lg:ml-64"}>
                <Header/>
                <main className={"p-6 lg:p-8"}>
                    {children}
                </main>
            </div>
        </div>
        </>
    )
}