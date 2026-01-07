from src.convert import normalize_spaces, normalize_emails, slugify

def test_normalize_spaces():
    assert normalize_spaces("Max Mustermann") == "Max Mustermann"
    assert normalize_spaces("   Max    Mustermann   ") == "Max Mustermann"
    assert normalize_spaces("") is None

def test_normalize_emails():
    assert normalize_emails("MAX@EXAMPLE.COM") == "max@example.com"
    assert normalize_emails("    erika@example.com    ") == "erika@example.com"
    assert normalize_emails("invalid-email") is None

def test_slugify():
    assert slugify("Max Mustermann") == "max-mustermann"
    assert slugify("  MAX   Mustermann   ") == "max-mustermann"
    assert slugify("") is None