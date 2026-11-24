"""Demonstração didática offline. Não acessa rede nem dispositivo real."""
from hashlib import sha256

# Bytes sintéticos produzidos localmente; nenhum firmware real é usado.
original = b"LAB-FIRMWARE-ORIGINAL-v1"
substituto = b"LAB-FIRMWARE-ALTERADO-v1"

# Modelo propositalmente inseguro: aceita qualquer pacote e não valida assinatura.
def insecure_install(package: bytes) -> bool:
    return bool(package)

print("DEMO DIDÁTICA OFFLINE - NÃO É TESTE DO NEXASENSE")
print(f"SHA-256 original:   {sha256(original).hexdigest()}")
print(f"SHA-256 substituto: {sha256(substituto).hexdigest()}")
print(f"Pacote alterado aceito pelo verificador fictício sem assinatura: {insecure_install(substituto)}")
print("Interpretação: ausência de validação permitiria aceitar bytes arbitrários neste modelo simplificado.")
print("Limite: não demonstra que qualquer firmware ou dispositivo real tenha essa falha.")
