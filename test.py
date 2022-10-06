# Make this work as either a package or not
if __name__ == "__main__":
	from charot.charot import charot
	print(charot())
else:
	from charot.charot import charot

def main():
	return charot()
