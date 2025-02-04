NAME=#PROJECT_NAME#

CC=cc
CXX=g++

LIBS=

INC_DIR=include/

LIBFLAGS=$(addprefix -l,$(LIBS))
INCLUDE_FLAGS=$(addprefix -I,$(INC_DIR))

include ./src/Makefile

OBJS=$(addprefix build/, $(filter %.o, $(SRCS:.cpp=.o) $(SRCS:.c=.o)))
CFLAGS=-Wall

all: $(OBJS)
	$(CXX) $^ -o $(NAME) $(LIBFLAGS) $(INCLUDE_FLAGS)

build/%.o: %.c
	mkdir -p $(dir $@)
	$(CC) -c $< -o $@

build/%.o: %.cpp
	mkdir -p $(dir $@)
	$(CXX) -c $< -o $@

clean:
	rm -rf $(NAME) build/
