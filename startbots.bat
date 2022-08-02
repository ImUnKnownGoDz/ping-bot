for %%f in (*.py) do (
	echo %%-nf
	start "" "%%f"
)
exit
