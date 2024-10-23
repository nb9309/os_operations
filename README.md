# os_operations

======================================================
				Working OS Based Operations with File and Folderss
======================================================
=>We know that OS is one of the Resources (Main Memory, Secondary Memory, Processor, Input Output Devices) 
   Allocation  and De-allocation Manager during Program Execution.
=>With OS, we can Perform the Following Operations.

		1. Create a Folder------------------------------------mkdir()
		2. Create  Folders Hierarchy ---------------------makedirs()
		3. Delete a Folder -----------------------------------rmdir()
		4. Delete Folders Hierarchy ---------------------removedirs()
		5. Remove a File Name----------------------------remove(File Name)
		6. Rename a Folder / File Name----------------rename(FileName/FolderName)
		7. Listing the Files in Folder.-------------------listdir()
=>To work with the above Operations, we use a pre-defined module called "os".

========================================================================================
Q. What is Difference Between Folder and File Name
ANS: Folder is one of the File Name and It does not Take Memory Space in Secondary Memory (HDD)
          File Name Takes Memory Space in Secondary Memory (HDD).
          
========================================================================================

--------------------------------------------------------------------------------------------
Creating Folder / Directory
--------------------------------------------------------------------------------------------
=>For Creating a Folder / Directory, we use  mkdir().
=>Syntax:   os.mkdir("Folder Name")
=>if the folder name already exist then we get FileExistsError
=>mkdir() can create only one folder at a time and if we try to create folderS hierarchy then 
    we get FileNotFoundError.
=>in mkdir(), if we specify any folder name with escape sequence ( \n \u \digits,\t..etc) then 
   we get OSError.


------------------------------------------------------------------------------------------------------------
Creating Folders Hierarchy.
-----------------------------------------------------------------------------------------------------------
=>For Creating Folders Hierarchy, we use makedirs().
=>Syntax:    os.makedirs("Folders Hierarchy")
=>Here Folders Hierarchy represent Root Folder\sub folder\sub-sub folder so on... 
=>if the folder name already exist then we get FileExistsError
=> if we specify any folder name with escape sequence ( \n \u \digits,\t..etc) then 
   we get OSError.

----------------------------------------------------------------------------------------------------------
Removing Folder / Directory.
----------------------------------------------------------------------------------------------------------
=>For Removing Folder / Directory, we use rmdir()
=>syntax: os.rmdir("folder name")
=>rmdir() can remove folder name provided folder name is empty.
=>if we specify any folder name with escape sequence ( \n \u \digits,\t..etc) then 
   we get OSError.
   
-------------------------------------------------------------------------------
Removing Folders Hierarchy. (removedirs() )
----------------------------------------------------------------------------------------------------------
=>For Removing Removing Folders Hierarchy, we use removedirs()
=>Syntax:    os.removedirs("Folders Hierarchy") 
=>Here Folders Hierarchy represent Root Folder\sub folder\sub-sub folder so on... 
=>if the folder name not  exist then we get FileNotFoundError
=> if we specify any folder name with escape sequence ( \n \u \digits,\t..etc) then 
   we get OSError.


---------------------------------------------------------------------------------------------------
Removing File Name from Folder.
---------------------------------------------------------------------------------------------------
=>To remove the file name from folder, we use remove()
=>Syntax:  os.remove("Absolute Path of File Name")
=>If the file name does not exist then we get FileNotFoundError


---------------------------------------------------------------------------------------------------
Renaming a Folder/File Name.
---------------------------------------------------------------------------------------------------
=>To rename a folder, we rename()
=>Syntax:  os.rename("Old Folder Name","New Folde Name")
=>Syntax:  os.rename("Old Folder Name","New Folde Name")
=>If the Old Folder Name does not exist then we get FileNotFoundError.


---------------------------------------------------------------------------------------------------
List the file names in folder.
---------------------------------------------------------------------------------------------------
=>To list the file names in folder, we use listdir()
=>Syntax:   os.listdir("Absolute Path of Folder Name")
=>If the Folder Name does not exist then we get FileNotFoundError.
