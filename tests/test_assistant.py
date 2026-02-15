from src.jarvis_assistant import JarvisAssistant


def test_low_risk_execution():
    assistant = JarvisAssistant()
    out = assistant.execute("Chrome'u aç ve google.com'a git")
    assert any("open_app" in line for line in out)


def test_high_risk_requires_confirmation():
    assistant = JarvisAssistant()
    out = assistant.execute("Bankadan para gönder")
    assert any("ONAY BEKLENİYOR" in line for line in out)
