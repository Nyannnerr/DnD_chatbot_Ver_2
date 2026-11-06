CC=gcc
CFLAGS=-fPIC -shared
TARGET=libengine.so

all: $(TARGET)

$(TARGET): engine.c
	$(CC) $(CFLAGS) -o $(TARGET) engine.c

clean:
	rm -f $(TARGET)
