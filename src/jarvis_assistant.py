from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class TaskStep:
    action: str
    args: str
    risk: RiskLevel = RiskLevel.LOW


class PolicyEngine:
    def requires_confirmation(self, step: TaskStep) -> bool:
        return step.risk in {RiskLevel.MEDIUM, RiskLevel.HIGH}


class Planner:
    def plan(self, command: str) -> List[TaskStep]:
        text = command.lower()
        steps: List[TaskStep] = []

        if "aç" in text and "chrome" in text:
            steps.append(TaskStep(action="open_app", args="chrome", risk=RiskLevel.LOW))

        if "git" in text and ("http" in text or ".com" in text):
            steps.append(TaskStep(action="open_url", args=command, risk=RiskLevel.LOW))

        if "yaz" in text:
            payload = command.split("yaz", maxsplit=1)[-1].strip(' "')
            if payload:
                steps.append(TaskStep(action="type_text", args=payload, risk=RiskLevel.LOW))

        if "sil" in text or "gönder" in text:
            steps.append(TaskStep(action="sensitive_action", args=command, risk=RiskLevel.HIGH))

        if not steps:
            steps.append(TaskStep(action="unknown", args=command, risk=RiskLevel.MEDIUM))

        return steps


class ToolRunner:
    def run(self, step: TaskStep) -> str:
        # Güvenli başlangıç için tüm eylemler simüle edilir.
        return f"[SIMULATED] {step.action} -> {step.args}"


class JarvisAssistant:
    def __init__(self) -> None:
        self.planner = Planner()
        self.policy = PolicyEngine()
        self.runner = ToolRunner()

    def execute(self, command: str, auto_confirm: bool = False) -> List[str]:
        results: List[str] = []
        steps = self.planner.plan(command)

        for step in steps:
            if self.policy.requires_confirmation(step) and not auto_confirm:
                results.append(f"[ONAY BEKLENİYOR] {step.action}: {step.args}")
                continue
            results.append(self.runner.run(step))

        return results


def main() -> None:
    assistant = JarvisAssistant()
    print("Jarvis benzeri asistan (MVP) hazır. Çıkmak için 'q' yaz.")

    while True:
        command = input("Komut > ").strip()
        if command.lower() in {"q", "quit", "exit"}:
            print("Görüşürüz.")
            break

        for line in assistant.execute(command):
            print("-", line)


if __name__ == "__main__":
    main()
