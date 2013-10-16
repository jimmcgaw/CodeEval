

class String {
	public:
		String(const char *value = 0);
		~String();

	private:
		char *data;
};