# Clean the project
clean:
	@ mkdir -p scripts/
	@ rm -rf scripts/*
	@ rm -rf failure.txt
	@ rm -rf success.txt
	@ echo "folder clean!"