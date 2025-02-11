import os
import shutil
import subprocess
from pathlib import Path

def create_template_file(src_main_java):
    """Create TemplateWithLog.java file."""
    template_content = """import velox.api.layer1.annotations.*;
import velox.api.layer1.common.Log;
import velox.api.layer1.data.InstrumentInfo;
import velox.api.layer1.simplified.*;

@Layer1SimpleAttachable
@Layer1StrategyName("Template with logs")
@Layer1ApiVersion(Layer1ApiVersionValue.VERSION1)
public class TemplateWithLog implements CustomModule {

    @Override
    public void initialize(String alias, InstrumentInfo info, Api api, InitialState initialState) {
        Log.info("Hello");
    }

    @Override
    public void stop() {
        Log.info("Bye");
    }
}"""

    with open(src_main_java / "TemplateWithLog.java", 'w') as f:
        f.write(template_content)

def create_maven_project(project_name, base_path):
    """Create a Maven-based Java project structure."""
    project_path = Path(base_path) / project_name

    # Create project directories
    src_main_java = project_path / "src" / "main" / "java"
    src_main_resources = project_path / "src" / "main" / "resources"
    src_test_java = project_path / "src" / "test" / "java"
    src_test_resources = project_path / "src" / "test" / "resources"

    for dir_path in [src_main_java, src_main_resources, src_test_java, src_test_resources]:
        dir_path.mkdir(parents=True, exist_ok=True)

    # Create template file
    create_template_file(src_main_java)

    # Create pom.xml with the specified content
    pom_content = f'''<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.bookmap</groupId>
    <artifactId>{project_name}</artifactId>
    <version>1.0-SNAPSHOT</version>
    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>${{java.version}}</maven.compiler.source>
        <maven.compiler.target>${{java.version}}</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.build.timestamp.format>yyyyMMdd-HHmmss</maven.build.timestamp.format>
    </properties>
    <repositories>
        <repository>
            <id>maven-bookmap</id>
            <url>https://maven.bookmap.com/maven2/releases/</url>
        </repository>
        <repository>
            <id>maven-central</id>
            <url>https://repo.maven.apache.org/maven2</url>
        </repository>
    </repositories>
    <dependencies>
        <dependency>
            <groupId>com.bookmap.api</groupId>
            <artifactId>api-core</artifactId>
            <version>7.5.0.19</version>
        </dependency>
        <dependency>
            <groupId>com.bookmap.api</groupId>
            <artifactId>api-simplified</artifactId>
            <version>7.5.0.19</version>
        </dependency>
    </dependencies>
    <build>
        <finalName>Bookmap_Add_On_${{maven.build.timestamp}}</finalName>
        <plugins>
            <plugin>
                <artifactId>maven-antrun-plugin</artifactId>
                <version>3.0.0</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <configuration>
                            <target>
                                <copy file="${{project.build.directory}}/Bookmap_Add_On_${{maven.build.timestamp}}.jar" todir="C:\\Bookmap\\addons\\my_addons"/>
                            </target>
                        </configuration>
                        <goals>
                            <goal>run</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>'''
    with open(project_path / "pom.xml", 'w') as f:
        f.write(pom_content)

def create_gitignore(project_path):
    """Create a .gitignore file for Java projects."""
    gitignore_content = """# Compiled class files
*.class

# Log files
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs
hs_err_pid*

# IDE-specific files
.idea/
*.iml
.vscode/
.project
.classpath
.settings/

# Build directories
target/
build/
bin/
out/

# Maven
target/
.mvn/
mvnw
mvnw.cmd
"""
    with open(project_path / ".gitignore", 'w') as f:
        f.write(gitignore_content)

def main():
    print("=== Java Project Creator ===")

    # Get project name
    while True:
        project_name = input("\nEnter project name (only letters, numbers, and hyphens allowed): ").strip()
        if project_name and all(c.isalnum() or c == '-' for c in project_name):
            break
        print("Invalid project name. Please try again.")

    # Get project location
    base_path = os.getcwd()
    project_path = Path(base_path) / project_name

    # Check if project directory already exists
    if project_path.exists():
        print(f"\nWarning: Directory '{project_name}' already exists!")
        overwrite = input("Do you want to overwrite it? (y/N): ").strip().lower()
        if overwrite != 'y':
            print("Project creation cancelled.")
            return
        shutil.rmtree(project_path)

    # Create project
    try:
        create_maven_project(project_name, base_path)
        create_gitignore(project_path)

        print(f"\nProject created successfully at: {project_path}")
        print("Created Maven project structure")
        print("Created pom.xml file")
        print("Created .gitignore file")
        print("Created TemplateWithLog.java template file")

        print("\nNext steps:")
        print("1. cd", project_name)
        print("2. mvn compile    # To compile the project")
        print("3. mvn test       # To run tests")
        print("4. mvn package    # To create the JAR file")

    except Exception as e:
        print(f"\nError creating project: {str(e)}")

if __name__ == "__main__":
    main()