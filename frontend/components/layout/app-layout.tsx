import { ReactNode } from "react";
import Sidebar from "./sidebar";
import Navbar from "./navbar";

interface AppLayoutProps {
  children: ReactNode;
}

export default function AppLayout({ children }: AppLayoutProps) {
  return (
    <div className="flex min-h-screen bg-muted/30">
      <Sidebar />

      <div className="flex flex-1 flex-col">
        <Navbar />

        <main className="flex-1 p-8">
          {children}
        </main>
      </div>
    </div>
  );
}