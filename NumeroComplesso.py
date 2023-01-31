class NumeroComplesso:

	def __init__(self,parteReale, parteImmaginaria):
		self.parteImmaginaria = parteImmaginaria
		self.parteReale = parteReale
		self.divisore = 1
		self.èDivisa = False

	def float getParteReale() {
		return parteReale / getDivisore();
	}

	public void setParteReale(float parteReale) {
		this.parteReale = parteReale;
	}

	public float getParteImmaginaria() {
		return parteImmaginaria / getDivisore();
	}

	public void setParteImmaginaria(float parteImmaginaria) {
		this.parteImmaginaria = parteImmaginaria;
	}

	public String getNumeroComplesso() {
		return parteReale + (èDivisa ? "/" + getDivisore() : "") + " + i(" + parteImmaginaria
				+ (èDivisa ? "/" + getDivisore() : "") + ")";
	}

	public float getDivisore() {
		return divisore;
	}

	public void setDivisore(float divisore) {
		this.divisore = divisore;
	}