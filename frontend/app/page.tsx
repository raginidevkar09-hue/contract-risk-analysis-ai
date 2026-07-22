import AppLayout from "@/components/layout/app-layout";
import { Card, CardContent } from "@/components/ui/card";
import {
  FileText,
  ShieldAlert,
  MessageSquare,
  TrendingUp,
} from "lucide-react";

const cards = [
  {
    title: "Contracts",
    value: "24",
    icon: FileText,
  },
  {
    title: "High Risks",
    value: "08",
    icon: ShieldAlert,
  },
  {
    title: "AI Chats",
    value: "56",
    icon: MessageSquare,
  },
  {
    title: "Health Score",
    value: "92%",
    icon: TrendingUp,
  },
];

export default function Home() {
  return (
    <AppLayout>
      <div className="space-y-8">
        <div>
          <h1 className="text-4xl font-bold">
            AI Contract Risk Analysis
          </h1>

          <p className="text-muted-foreground mt-2">
            Welcome back. Here is an overview of your workspace.
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
          {cards.map((card) => {
            const Icon = card.icon;

            return (
              <Card key={card.title}>
                <CardContent className="flex items-center justify-between p-6">
                  <div>
                    <p className="text-sm text-muted-foreground">
                      {card.title}
                    </p>

                    <h2 className="mt-2 text-3xl font-bold">
                      {card.value}
                    </h2>
                  </div>

                  <div className="rounded-xl bg-blue-100 p-3">
                    <Icon className="h-6 w-6 text-blue-600" />
                  </div>
                </CardContent>
              </Card>
            );
          })}
        </div>
      </div>
    </AppLayout>
  );
}