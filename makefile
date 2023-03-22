# Clean the project
clean:
	@ mkdir -p scripts/
	@ rm -rf scripts/*
	@ rm -rf error_packetdrill.log
	@ rm -rf error_target.log
	@ rm -rf success.log
	@ echo "folder clean!"