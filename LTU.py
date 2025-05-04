class CacheLRU:

    def __init__(self, cache_size, ram_size):
        self.cache_size = cache_size
        self.ram_size = ram_size

        self.cache = {}  # dicionário vazio para representar a cache
        self.ram = {}    # dicionário vazio para representar a RAM
        self.lista_lru = []  # lista para controlar o LRU

        self.popular_ram()  # corrigido: `self.` estava faltando

    def popular_ram(self):
        for i in range(self.ram_size):
            self.ram[i] = i

    def exibir_ram(self):
        print("RAM:", self.ram)

    def exibir_cache(self):
        print("Cache:", self.cache)

    def buscar_cache(self, address, novo_valor=None):
        print(f"\nBuscando o endereço: {address} ...")

        # Cache vazia
        if len(self.cache) == 0:
            print("Cache vazia ;-;")
        
        # Cache hit
        if address in self.cache:
            print("Cache hit :D")

            if novo_valor is not None:
                self.cache[address] = novo_valor

            # Atualiza a ordem de uso
            self.lista_lru.remove(address)
            self.lista_lru.append(address)

        else:
            print("Cache miss ;-;")

            # Se a cache estiver cheia, remover o LRU
            if len(self.cache) >= self.cache_size:
                lru = self.lista_lru.pop(0)
                print(f"Substituindo endereço da LRU: {lru} da cache")

                # Atualiza a RAM com o valor que estava na cache
                self.ram[lru] = self.cache[lru]
                del self.cache[lru]

            # Busca o valor da RAM
            valor = self.ram.get(address, 0)

            if novo_valor is not None:
                valor = novo_valor

            self.cache[address] = valor
            self.lista_lru.append(address)

    def atualizar_ram_com_cache(self):
        print("\nAtualizando RAM com os valores da cache ...")
        for endereco in self.cache:
            self.ram[endereco] = self.cache[endereco]


# Testando a classe
cs = CacheLRU(4, 16)

cs.exibir_ram()
cs.exibir_cache()

cs.buscar_cache(5, 1)
cs.exibir_cache()

cs.buscar_cache(9, 2)
cs.exibir_cache()

cs.buscar_cache(8, 3)
cs.exibir_cache()

cs.buscar_cache(1, 4)
cs.exibir_cache()

# Próxima chamada causará substituição LRU
cs.buscar_cache(6, 9)
cs.exibir_cache()

# Atualizar RAM
cs.atualizar_ram_com_cache()
cs.exibir_ram()

