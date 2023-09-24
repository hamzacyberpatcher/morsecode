import sys

morsekey = {
	'a' : '._',
	'b' : '_...',
	'c' : '_._.',
	'd' : '_..',
	'e' : '.',
	'f' : '.._.',
	'g' : '__.',
	'h' : '....',
	'i' : '..',
	'j' : '.___',
	'k' : '_._',
	'l' : '._..',
	'm' : '__',
	'n' : '_.',
	'o' : '___',
	'p' : '.__.',
	'q' : '__._',
	'r' : '._.',
	's' : '...',
	't' : '_',
	'u' : '.._',
	'v' : '..._',
	'w' : '.__',
	'x' : '_.._',
	'y' : '_.__',
	'z' : '__..',
	'1' : '.____',
	'2' : '..___',
	'3' : '...__',
	'4' : '...._',
	'5' : '.....',
	'6' : '_....',
	'7' : '__...',
	'8' : '___..',
	'9' : '____.',
	'0' : '_____',
	'?' : '..__..',
	'!' : '_._.__',
	'.' : '._._._',
	',' : '__..__',
	';' : '_._._.',
	':' : '___...',
	'+' : '._._.',
	'-' : '_...._',
	'/' : '_.._.',
	'=' : '_..._',
	'&' : '.-...',
	"'" : '.----.',
	'@' : '.--.-.',
	')' : '-.--.-',
	'(' : '-.--.'
	}
def morse_encrypt(text):
	text = text.lower()
	encrypt = ""
	for c in text:
		if c == " ":
			encrypt = encrypt + "/" + " "
			continue
		if c not in morsekey:
			print("Cannot translate the character : ",c)
			return 1
		encrypt = encrypt + morsekey[c] + " "
	return encrypt

def morse_decrypt(text):
	decryptkey = {v: k for k, v in morsekey.items()}
	decryptkey["/"] = " "
	decrypt = ""
	for word in text.split():
		if word not in decryptkey:
			decrypt = decrypt + "#"
			continue
		decrypt = decrypt + decryptkey[word]
	return decrypt.upper()

def main():
	if len(sys.argv) != 3:
		print("Usage : morse.py <mode> <text>")
		print("mode: 1 for encryption and 2 for decryption")
		print("Note: Enclose the text within ()")
		return 1
	mode = sys.argv[1]
	text = sys.argv[2]
	if mode == '1':
		encrypt = morse_encrypt(text)
		if encrypt == 1:
			return 1
		print("Morse Code : ",encrypt)
	elif mode == '2':
		decrypt = morse_decrypt(text)
		print("Text : ",decrypt)
	else:
		print("not a valid mode")
		return 1
if __name__ == "__main__":
	main()